from src.TerminalBanner import Terminal_banner
from random import choice;from url64 import * ;
from stringcolor import *;

api =  open("src/apikey.cfg","r").readline();
def rand_colors():
    return choice([
        "#bfff00","#80ff00","#40ff00","#40ff00",
        "#00ff00","#00bfff","#0080ff","#4000ff",
        "#8000ff","#ff00ff","#ff0040","#ff0000"]); 
banner = cs("""
                    ,mMm.,------.,mMm.
                    (GNP'        `?ND)
                     P  dMm.  ,mMb  ?
                     (  ?X_O  O_XP  )
                     (      qp      ) checker
                      \  `--'`--'  /
                   mails            ,__)
                  (--|__) _.._  _| _,
                    _|   (_|| |(_|(_|
                   (""",rand_colors())
def xusr():
    xfzdq = Terminal_banner(string="<Email> <Mode>",font="lalia",
    decoration="barcode1",color=rand_colors(),bg_color=None).textArt;
    xf00a = Terminal_banner(decoration="champion1",
    reverse=False,color=rand_colors(),bg_color=None).decoration
    query = "\t    %s\n   %s\n   %s "%(xfzdq,xf00a,xf00a);
    return query;

def xhelp():
    return cs("""
      <mail>  <mode>  <args>

    mode  : random,list,check.

    random mode : example@mail.com random abc > menggunakan random string,
    lists mode : example@mail.com lists file.txt > menggunakan list dalam file,
    check mode : example@mail.com check > checking,
    
    api : https://developers.neverbounce.com
    key : src/apikey.cfg

    YouTube : https://www.youtube.com/channel/UCCkFPWbQaqonPc51uVeKvyg
    Github : https://github.com/ExsoKamabay

    """,rand_colors());

def random_check(strg="abc"):
    acak = [strg[0],strg[1],strg[2]];
    pack = (choice(acak)+choice(acak)+choice(acak));
    return pack;

def read_file(file):
    with open(file,"r") as f:
        return f.read();
def invalid():
    return cs("\t\tKeyword salah!,ketikan 'help me':)","red")