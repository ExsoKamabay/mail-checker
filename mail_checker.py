from src import * ; from src.inc import * ;
from  src.TerminalBanner import Terminal_banner ;
class mailChecker:
    def __init__(self):
        print(banner);
    def check(self):
        setattr(self,"user",(input(xusr()).split()));
        if not getattr(self,"user"):
            print(Terminal_banner(string="\t\t\tKOSONG!\n",font="lalia",
            color=rand_colors(),bg_color=None,decoration=None).strings);
        elif getattr(self,"user")[1] == str("random"):
            start,stop = int(0),int(1)
            while start < 10:
                setattr(self,"getInfo",(
                client(api_key=decode(api),timeout=10).single_check(
                    getattr(self,"user")[0].replace("*",random_check(
                        getattr(self,"user")[2]
                    )),True,True,True)));
                setattr(self,"out",("\nEmail : %s\nStatus : %s\nHost : %s\nResult : %s\nExec time : %s\n"%(
                    getattr(self,"getInfo")["address_info"]["original_email"],
                    getattr(self,"getInfo")["status"],getattr(self,"getInfo")["address_info"]["host"],
                    getattr(self,"getInfo")["result"],getattr(self,"getInfo")["execution_time"])));
                if getattr(self,"getInfo")["result"] == str("valid"):print(cs(getattr(self,"out"),"#40ff00"));
                else:print(cs(getattr(self,"out"),"#ff4000"));
                start+=stop;
        elif getattr(self,"user")[1] == str("file"):
            setattr(self,"read",(read_file(getattr(self,"user")[2]).split()));
            for check in getattr(self,"read"):
                setattr(self,"getInfo",(
                client(api_key=decode(api),timeout=10).single_check(
                    getattr(self,"user")[0].replace("*",check),True,True,True)));
                setattr(self,"out",("\nEmail : %s\nStatus : %s\nHost : %s\nResult : %s\nExec time : %s\n"%(
                    getattr(self,"getInfo")["address_info"]["original_email"],
                    getattr(self,"getInfo")["status"],getattr(self,"getInfo")["address_info"]["host"],
                    getattr(self,"getInfo")["result"],getattr(self,"getInfo")["execution_time"])));
                if getattr(self,"getInfo")["result"] == str("valid"):print(cs(getattr(self,"out"),"#40ff00"));
                else:print(cs(getattr(self,"out"),"#ff4000"));
        elif getattr(self,"user")[1] == str("check"):
            setattr(self,"getInfo",(client(
                api_key=decode(api),timeout=3
            ).single_check(getattr(self,"user")[0],
            True,True,True)));
            setattr(self,"out",("\nEmail : %s\nStatus : %s\nHost : %s\nResult : %s\nExec time : %s\n"%(
                getattr(self,"getInfo")["address_info"]["original_email"],
                getattr(self,"getInfo")["status"],getattr(self,"getInfo")["address_info"]["host"],
                getattr(self,"getInfo")["result"],getattr(self,"getInfo")["execution_time"])));
            if getattr(self,"getInfo")["result"] == str("valid"):print(cs(getattr(self,"out"),"#40ff00"));
            else:print(cs(getattr(self,"out"),"#ff4000"));
        elif getattr(self,"user")[0] == str("help") or getattr(self,"user")[1] == str("me"):
            print(xhelp(),"\t     ",cs("Mail Valid","#40ff00")," - ",cs("Mail Invalid","#ff4000"));
        self.check();
if __name__=="__main__":
    try:
        mailChecker().check()
    except:print(invalid());