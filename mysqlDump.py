#coding:utf-8
#!/usr/bin/python
import os
import sys

def read_info(filePath):
	fp = open(filePath, 'r')
	dbHost = []
	dbUser = []
	dbPass = []
	lines = fp.readlines()
	for data in lines:
		host, username, password = data.split(',')
		host = host.strip('\t\r\n')
		username = username.strip('\t\r\n')
		password = password.strip('\t\r\n')
		dbHost.append(host)
		dbUser.append(username)
		dbPass.append(password)
	fp.close()
	return dbHost, dbUser, dbPass

def dump(saveFilePath, dbHost, dbUser, dbPass):
	exportFile = dbHost + '.sql'
	sqlFormat = "mysqldump --all-databases --skip-lock-tables -h%s -u%s -p%s > %s"
	sql = (sqlFormat%(dbHost, dbUser, dbPass, exportFile))
	command = os.popen(sql)
	print '\033[1;31;40m'
	print dbHost
	print '\033[0m'
	print command.read()

def delEmpty():
	os.popen("find . -name '*' -type f -size 0c | xargs -n 1 rm -f")

def main():
	filePath = raw_input("please input db_info's filepath:\n")
	saveFilePath = 'mysqlDump'
	if not os.path.exists(saveFilePath):
		os.mkdir(saveFilePath)
		os.chdir(saveFilePath)
	resultDataInfo = read_info(filePath)
	for len_first in range(0, len(resultDataInfo[0])):
		dbHost = resultDataInfo[0][len_first]
		dbUser = resultDataInfo[1][len_first]
		dbPass = resultDataInfo[2][len_first]
		#result = dump(saveFilePath, dbHost, dbUser, dbPass)
		dump(saveFilePath, dbHost, dbUser, dbPass)
	delEmpty()

if __name__ == '__main__':
	main()
