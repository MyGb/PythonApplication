#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import requests
import threading
from requests import RequestException
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,Text,Integer,create_engine

"""
职位分析
请求地址：
	https://www.lagou.com/jobs/list_android?px=default&city=重庆
	https://www.lagou.com/jobs/positionAjax.json?px=default&city=重庆&needAddtionalResult=false
"""
headers = {
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate, sdch, br",
		"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
		"Cache-Control":"max-age=0",
		"Connection":"keep-alive",
		"Cookie":"LGUID=20151023224909-37979b56-7995-11e5-8ef1-5254005c3644; tencentSig=8667215872; user_trace_token=20170212164900-02a892dae24b4db6aa76ba88a355ced8; index_location_city=%E4%B8%8A%E6%B5%B7; JSESSIONID=13EFFA3ADA58F50C292815348A720B43; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=search_code; SEARCH_ID=087fc7d565514b11af6390452ebbdf7d; _ga=GA1.2.689182724.1445611739; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1486889385,1486889581,1488615828,1488694233; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1488694766; LGSID=20170305140943-531ce896-016a-11e7-b18c-525400f775ce; LGRID=20170305141835-908ea2b3-016b-11e7-91ba-5254005c3644",
		"Host":"www.lagou.com",
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}

url = "https://www.lagou.com/jobs/positionAjax.json"

Base = declarative_base()

class Job(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True,autoincrement=True)
    positionName = Column(Text,)
    salary = Column(String(10))
    workYear = Column(String(10))
    education = Column(String(10))
    industryField = Column(String(40))
    companyShortName = Column(String(100))
    companyFullName = Column(Text,)
    city = Column(String(20))
    district = Column(String(20))
    businessZones = Column(Text,)
    financeStage = Column(Text,)
    companyLabelList = Column(Text,)

def dictToObject(jobDict):
	"""把Dict对象转为Job对象"""
	positionName = jobDict["positionName"]
	salary = jobDict["salary"]
	workYear = jobDict["workYear"]
	education = jobDict["education"]
	industryField = jobDict["industryField"]
	companyShortName = jobDict["companyShortName"]
	companyFullName = jobDict["companyFullName"]
	city = jobDict["city"]
	district = jobDict["district"]

	businessZones = ""
	if jobDict["businessZones"]:
		for bz in jobDict["businessZones"]:
			businessZones = businessZones + bz.strip()
			if bz != jobDict["businessZones"][-1]:
				businessZones = businessZones + "/"

	financeStage = jobDict["financeStage"]

	companyLabelList = ""
	if jobDict["companyLabelList"]:
		for label in jobDict["companyLabelList"]:
			companyLabelList = companyLabelList+label.strip()
			if label != jobDict["companyLabelList"][-1]:
				companyLabelList = companyLabelList + "/"
				
	job = Job(positionName = positionName,
				salary = salary,
				workYear = workYear,
				education = education,
				industryField = industryField,
				companyShortName = companyShortName,
				companyFullName = companyFullName,
				city = city,
				district = district,
				businessZones = businessZones,
				financeStage = financeStage,
				companyLabelList = companyLabelList)
	return job

def requestContentByPost(formData,queryParameters):
	"""通过Post方式请求内容"""
	try:
		req = requests.post(url,headers=headers,params=queryParameters,data=formData)
		if req.status_code == 200:
			content = req.json()
	except RequestException as e:
		pass
	else:
		return content



def handleResult(result):
	"""处理返回结果，抽取有用的字段，把信息保存到数据库中"""
	try:
		engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/python_test')
		Base.metadata.create_all(engine)
		DBSession = sessionmaker(bind=engine)
		session = DBSession()

		for jobDict in result:
			job = dictToObject(jobDict)
			session.add(job)

		session.commit()
	except Exception as e:
		print(e)
	finally:
		session.close()

def work(formData,queryParameters):
	result = requestContentByPost(formData,queryParameters)
	if !result:
		return
	handleData = result["content"]["positionResult"]["result"]
	thread = threading.Thread(target=handleResult,args=(handleData,))
	thread.start()
	return result
	
def startWork(formData,queryParameters):
	result = work(formData,queryParameters)
	if !result:
		return
	totalCount = result["content"]["positionResult"]["totalCount"] #总记录条数
	resultSize = result["content"]["positionResult"]["resultSize"] #每页显示数
	if totalCount == resultSize:
		return
	page = totalCount // resultSize
	if totalCount % resultSize != 0:
		page = page + 1
	for pn in range(2,page+1):
		tempFormData = {"first":"false","pn":str(pn),"kd":"Python"}
		thread = threading.Thread(target=work,args=(tempFormData,queryParameters))
		thread.start()



if __name__=="__main__":
	#"北京","重庆","Android","java"
	cities = ("上海",)
	jobs = ("Python",)
	formData = {"first":"false","pn":"1","kd":"Python"}
	for job in jobs:
		formData = {"first":"false","pn":"1","kd":job}
		for city in cities:
			queryParameters = {"px":"default","city":city,"needAddtionalResult":"false"}
			thread = threading.Thread(target=startWork,args=(formData,queryParameters))
			thread.start()