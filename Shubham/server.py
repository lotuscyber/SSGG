
import os

print ("wait a second")

os.system ("mkdir -p $PREFIX/var/lib/postgresql")
os.system ("initdb $PREFIX/var/lib/postgresql")

os.system ("pg_ctl -D $PREFIX/var/lib/postgresql start")

print ("coded by VPP Hacker")
