import paramiko
import datetime as dt
import fnmatch

tdy_dt = dt.date.today()
dy = tdy_dt.strftime('%d')
mon = tdy_dt.strftime('%m')
yr = tdy_dt.strftime('%Y')
yr2 = tdy_dt.strftime('%y')
curr_dy = yr + mon + dy

def downloadFromSftp():
    host = 'host'
    username = 'username'
    password = 'pw'
    port = port_num
    log_path = 'path'
    log_file = 'log_file' + curr_dy + '.txt'
    paramiko.util.log_to_file(log_path + log_file)
    sftpTransport = paramiko.Transport((host, port))
    sftpTransport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(sftpTransport)
    for file in sftp.listdir('~/folder/that_contains/place/to_get':
        if fnmatch.fnmatch(file,'*'+'file_extension_needed'+curr_dy+'*')==True:
            sftpPath = '~/folder/' + file
            localPath = '~/home/folder' + file
            sftp.get(sftpPath, localPath)
        if fnmatch.fnmatch(file,'*'+'ET4_'+curr_dy+'*')==True:
            sftpPath = '~/folder/' + file
            localPath = '~/home/folder' + file
            sftp.get(sftpPath, localPath)
        if fnmatch.fnmatch(file,'*'+curr_dy+'*')==True:
            sftpPath = '~/folder/' + file
            localPath = '~/home/folder' + file
            sftp.get(sftpPath, localPath)
        if fnmatch.fnmatch(file,'*'+curr_dy+'*')==True:
            sftpPath = '~/folder/' + file
            localPath = '~/home/folder' + file
            sftp.get(sftpPath, localPath)
    sftp.close()
    sftpTransport.close()


if __name__ == "__main__":
    downloadFromSftp()
