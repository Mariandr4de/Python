from ftplib import *

ftp_ativo=Falseftp= FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

ftp.quit()