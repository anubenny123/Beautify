from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import MySQLdb
import webbrowser
from django.contrib import messages

from numpy import place

db=MySQLdb.connect("localhost","root","","dbbeautify")
c=db.cursor()

######################################################################
#                           SMS FUNCTION
######################################################################
def sendsms(ph,msg):
    sendToPhoneNumber= ph
    url = "http://sms.mdsmedia.in/http-api.php?username=7000183&password=LCCCOK123&senderid=LCCEKM&route=23&number="+sendToPhoneNumber+"&message="+msg
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)
######################################################################
#                                                                    #
#                                                                    #
#                           COMMON                                   #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    return render(request,"index.html")
######################################################################
#                           LOAD LOGIN PAGE
######################################################################
def login(request):
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where uname='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where uname='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="parlour"):
                        return HttpResponseRedirect("/parlourhome")
                    elif(i[2]=="customer"):
                        return HttpResponseRedirect("/customerhome")
                    
                elif(i[3]=="inactive"):
                    msg="Your registration is incomplete. Please register"
                else:
                    msg="You are not authenticated to login"
            else:
                msg="Incorrect password"
        else:
            msg="User doesnt exist"
    return render(request,"commonlogin.html",{"msg":msg})
######################################################################
#                   LOAD LAB REGISTRATION PAGE
######################################################################
def parlour(request):
    msg=""
    if(request.POST):
        name=request.POST['txtName']
        address=request.POST['txtAddress']
        email=request.POST['txtEmail']
        contact=request.POST['txtContact']
        lic=request.POST['txtLicense']
        pwd=request.POST['txtPassword']
        place=request.POST['txtplace']
        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)
        
        s="insert into tblparlour (pName,pAddress,pEmail,pContact,pLicense,pDistrict,pImg) values('"+name+"','"+address+"','"+email+"','"+contact+"','"+lic+"','"+place+"','"+uploaded_file_url+"')"
        print(s)
        try:
            c.execute(s)
        except:
            msg="Sorry registration error"
        else:
            s="insert into tbllogin (uname,pwd,utype,status) values('"+email+"','"+pwd+"','parlour','0')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Registration successfull. Wait for approval"
    return render(request,"commonparlour.html",{"msg":msg})
######################################################################
#                   LOAD LAB REGISTRATION PAGE
######################################################################
def customer(request):
    msg=""
    if(request.POST):
        name=request.POST['txtName']
        address=request.POST['txtAddress']
        email=request.POST['txtEmail']
        contact=request.POST['txtContact']
        
        pwd=request.POST['txtPassword']
        place=request.POST['txtplace']
        
        
        s="insert into tblcustomer (cName,cAddress,cEmail,cContact,cDistrict) values('"+name+"','"+address+"','"+email+"','"+contact+"','"+place+"')"
        print(s)
        try:
            c.execute(s)
        except:
            msg="Sorry registration error"
        else:
            s="insert into tbllogin (uname,pwd,utype,status) values('"+email+"','"+pwd+"','customer','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Registration successfull. Login to continue"
    return render(request,"commoncustomer.html",{"msg":msg})
######################################################################
#                                                                    #
#                                                                    #
#                           ADMIN                                    #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD ADMIN PAGE
######################################################################
def adminhome(request):
    return render(request,"adminhome.html")
def adminparlour(request):
    s="select * from tblparlour where pEmail in(select uname from tbllogin where status='0')"
    c.execute(s)
    data=c.fetchall()
    s="select * from tblparlour where pEmail in(select uname from tbllogin where status='1')"
    c.execute(s)
    data1=c.fetchall()
    return render(request,"adminparlour.html",{"data":data,"data1":data1})
def updateuser(request):
    email=request.GET.get("id")
    status=request.GET.get("status")
    url=request.GET.get("url")
    s="update tbllogin set status='"+status+"' where uname='"+email+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect(url)
def admincustomer(request):
    s="select * from tblcustomer where cEmail in(select uname from tbllogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    return render(request,"admincustomer.html",{"data":data})
def adminfeedback(request):
    s="select tblcustomerreview.*,tblcustomer.cName,tblparlour.pName from tblcustomerreview,tblcustomer,tblparlour where tblcustomerreview.cEmail=tblcustomer.cEmail and tblcustomerreview.pEmail=tblparlour.pEmail"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminfeedback.html",{"data":data})
######################################################################
#                                                                    #
#                                                                    #
#                           PARLOUR                                    #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD PARLOUR PAGE
######################################################################
def parlourhome(request):
    return render(request,"parlourhome.html")
######################################################################
#                      LOAD PARLOUR CATEGORY
######################################################################
def parlourcategory(request):
    email=request.session['email']
    msg=""
    if request.POST:
        cat=request.POST["txtCategory"]
        s="insert into tblcategory(pEmail,category,status) values('"+email+"','"+cat+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Category added"
    s="select * from tblcategory where pEmail='"+email+"' and status='1'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"parlourcategory.html",{"data":data,"msg":msg})
def deletecat(request):
    cid=request.GET.get("id")
    s="update tblcategory set status='0' where catid='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/parlourcategory")
######################################################################
#                           LOAD PARLOUR TREATMENT
######################################################################
def parlourtreatment(request):
    email=request.session['email']
    msg=""
    if request.POST:
        cat=request.POST["cat"]
        name=request.POST["txtName"]
        gender=request.POST["gender"]
        desc=request.POST["txtDesc"]
        rate=request.POST["txtRate"]

        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)

        s="insert into tbltreatment(catid,tName,gCat,tDesc,tRate,tImg,status) values('"+cat+"','"+name+"','"+gender+"','"+desc+"','"+rate+"','"+uploaded_file_url+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Treatment added"
    s="select * from tblcategory where pEmail='"+email+"' and status='1'"
    c.execute(s)
    cat=c.fetchall()
    s="select * from tbltreatment where catid in(select catid from tblcategory where pEmail='"+email+"' and status='1') and status='1'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"parlourtreatment.html",{"data":data,"msg":msg,"cat":cat})
def deletetreatment(request):
    cid=request.GET.get("id")
    s="update tbltreatment set status='0' where tId='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/parlourtreatment")
######################################################################
#                           LOAD PARLOUR PACKAGE
######################################################################
def parlourpackage(request):
    email=request.session['email']
    msg=""
    if request.POST:
        
        name=request.POST["txtName"]
        gender=request.POST["gender"]
        desc=request.POST["txtDesc"]
        rate=request.POST["txtRate"]
        s="insert into tblpackage(pEmail,packName,packGend,packDesc,packRate,status) values('"+email+"','"+name+"','"+gender+"','"+desc+"','"+rate+"','1')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Package added"
            s="select max(packId) from tblpackage"
            c.execute(s)
            d=c.fetchone()
            packid=d[0]
            return HttpResponseRedirect("/selectpackage?id="+str(packid))

    s="select * from tblpackage where pEmail='"+email+"' and status='1'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"parlourpackage.html",{"data":data,"msg":msg})
def delpackage(request):
    cid=request.GET.get("id")
    s="update tblpackage set status='0' where packId='"+cid+"'"
    c.execute(s)
    s="delete from tblpackagetreament where packId='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/parlourpackage")
def selectpackage(request):
    packid=request.GET.get("id")
    email=request.session['email']
    s="select * from tbltreatment where catid in(select catid from tblcategory where pEmail='"+email+"' and status='1') and status='1'"
    c.execute(s)
    print(s)
    data=c.fetchall()
    if request.POST:
        com=request.POST.getlist("com")
        for i in com:
            s="select count(*) from tblpackagetreatment where packId='"+str(packid)+"' and tId='"+str(i)+"'"
            c.execute(s)
            d=c.fetchone()
            count=d[0]
            if count==0:
                s="insert into tblpackagetreatment(packId,tId) values('"+str(packid)+"','"+str(i)+"')"
                c.execute(s)
            db.commit()
        return HttpResponseRedirect("/parlourpackage")
    return render(request,"parlourpackagetreatment.html",{"data":data})
def viewpackage(request):
    packid=request.GET.get("id")
    s="select tName from tbltreatment where tId in(select tId from tblpackagetreatment where packId='"+packid+"')"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        return HttpResponseRedirect("/selectpackage?id="+packid)
    return render(request,"parlourviewtreatment.html",{"data":data})
######################################################################
#                           LOAD PARLOUR OFFER
######################################################################
def parlouroffer(request):
    email=request.session['email']
    msg=""
    if request.POST:
        
        name=request.POST["txtName"]
        
        desc=request.POST["txtDesc"]
        rate=request.POST["txtRate"]
        fdate=request.POST["txtFrom"]
        tdate=request.POST["txtTo"]
        s="insert into tbloffer(pEmail,oName,oDesc,oRate,oFrom,oTo) values('"+email+"','"+name+"','"+desc+"','"+rate+"','"+fdate+"','"+tdate+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Offer added"
            s="select max(oId) from tbloffer"
            c.execute(s)
            d=c.fetchone()
            packid=d[0]
            return HttpResponseRedirect("/selectoffer?id="+str(packid))

    s="select * from tbloffer where pEmail='"+email+"' order by oId desc"
    c.execute(s)
    data=c.fetchall()
    return render(request,"parlouroffer.html",{"data":data,"msg":msg})

def selectoffer(request):
    packid=request.GET.get("id")
    email=request.session['email']
    s="select * from tbltreatment where catid in(select catid from tblcategory where pEmail='"+email+"' and status='1') and status='1'"
    c.execute(s)
    print(s)
    data=c.fetchall()
    if request.POST:
        com=request.POST.getlist("com")
        for i in com:
            s="select count(*) from tbloffertreatment where oId='"+str(packid)+"' and tId='"+str(i)+"'"
            c.execute(s)
            d=c.fetchone()
            count=d[0]
            if count==0:
                s="insert into tbloffertreatment(oId,tId) values('"+str(packid)+"','"+str(i)+"')"
                c.execute(s)
            db.commit()
        return HttpResponseRedirect("/parlouroffer")
    return render(request,"parlouroffertreatment.html",{"data":data})
def viewoffer(request):
    packid=request.GET.get("id")
    s="select tName from tbltreatment where tId in(select tId from tbloffertreatment where oId='"+packid+"')"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        return HttpResponseRedirect("/selectoffer?id="+packid)
    return render(request,"parlourviewoffer.html",{"data":data})
def parlourbooking(request):
    email=request.session['email']
    s="select tbloffer.oName,tblcustomer.cName,tblofferbooking.bdate,tblofferbooking.status,tblofferbooking.obookid,tblofferbooking.btime from tbloffer,tblcustomer,tblofferbooking where tbloffer.oId=tblofferbooking.oId and tbloffer.pEmail='"+email+"' and tblofferbooking.cEmail=tblcustomer.cEmail"
    c.execute(s)
    offer=c.fetchall()
    s="select tblpackage.packName,tblcustomer.cName,tblpackagebooking.bdate,tblpackagebooking.status,tblpackagebooking.pbid,tblpackagebooking.btime from tblpackage,tblcustomer,tblpackagebooking where tblpackage.packId=tblpackagebooking.packId and tblpackage.pEmail='"+email+"' and tblpackagebooking.cEmail=tblcustomer.cEmail"
    c.execute(s)
    package=c.fetchall()
    s="select tbltreatment.tName,tblcustomer.cName,tbltreatmentbooking.bdate,tbltreatmentbooking.status,tbltreatmentbooking.tbid,tbltreatmentbooking.btime from tbltreatment,tblcustomer,tbltreatmentbooking,tblcategory where tbltreatment.tId=tbltreatmentbooking.tId and tbltreatment.catid=tblcategory.catid and tblcategory.pEmail='"+email+"' and tbltreatmentbooking.cEmail=tblcustomer.cEmail"
    c.execute(s)
    treatment=c.fetchall()
    return render(request,"parlourbooking.html",{"offer":offer,"package":package,"treatment":treatment})
def updatebooking(request):
    bid=request.GET.get("id")
    btype=request.GET.get("type")
    if btype=="offer":
        s="update tblofferbooking set status='payment recieved' where obookid='"+bid+"'"
    elif btype=="package":
        s="update tblpackagebooking set status='payment recieved' where pbid='"+bid+"'"
    elif btype=="treatment":
        s="update tbltreatmentbooking set status='payment recieved' where tbid='"+bid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/parlourbooking")
######################################################################
#                           LOAD PARLOURS FOR CUSTOMER
######################################################################
def parlourfeedback(request):
    email=request.session['email']
    s="select tblcustomerreview.*,tblcustomer.cName from tblcustomerreview,tblcustomer where tblcustomerreview.cEmail=tblcustomer.cEmail and tblcustomerreview.pEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"parlourfeedback.html",{"data":data})
    
        
    
    
######################################################################
#                                                                    #
#                                                                    #
#                           CUSTOMER                                 #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD CUSTOMER PAGE
######################################################################
def customerhome(request):
    email=request.session["email"]
    s="Select cDistrict from tblcustomer where cEmail='"+email+"'"
    c.execute(s)
    d=c.fetchone()
    dist=d[0]
    s="select count(*) from tbloffer,tblparlour where tbloffer.pEmail=tblparlour.pEmail and tblparlour.pDistrict='"+dist+"' and tbloffer.oTo>(select sysdate())"
    c.execute(s)
    d=c.fetchone()
    count=d[0]
    s="select tbloffer.oName,tbloffer.oRate,tblparlour.pName,tbloffer.oId from tbloffer,tblparlour where tbloffer.pEmail=tblparlour.pEmail and tblparlour.pDistrict='"+dist+"' and tbloffer.oTo>(select sysdate())"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerhome.html",{"data":data,"count":count})
def customerofferdetails(request):
    oid=request.GET.get("id")
    s="select tbloffer.*,tblparlour.* from tbloffer,tblparlour where tbloffer.pEmail=tblparlour.pEmail and tbloffer.oId='"+oid+"'"
    c.execute(s)
    offer=c.fetchall()
    s="select tName,tImg from tbltreatment where tId in(select tId from tbloffertreatment where oId='"+oid+"')"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        return HttpResponseRedirect("/customerchoosedate?id="+str(oid)+"&type=offer")
    return render(request,"customerofferdetails.html",{"data":data,"offer":offer})
def customerchoosedate(request):
    oid=request.GET.get("id")
    btype=request.GET.get("type")
    email=request.session["email"]
    s="select cContact from tblcustomer where cEmail='"+email+"'"
    print(s)
    c.execute(s)
    d=c.fetchone()
    contact=d[0]
    if request.POST:
        bdate=request.POST['txtDate']
        btime=request.POST['txtTime']
        if btype=="offer":
            s="select pEmail from  tbloffer where oId='"+oid+"'"
            c.execute(s)
            d=c.fetchone()
            pemail=d[0]
            s="select count(*) from tblofferbooking where bdate='"+bdate+"' and oId in(select oId from tbloffer where pEmail='"+pemail+"')"
            c.execute(s)
            d=c.fetchone()
            # btime=request.POST['txtTime']
            # btime="10:00AM"
            if(d[0]>0):
                s="select max(tbId) from tblofferbooking where bdate='"+btime+"' and oId in(select oId from tbloffer where pEmail='"+pemail+"')"
                c.execute(s)
                d=c.fetchone()
                bid=d[0]
                s="select bTime from tblofferbooking where obookId='"+bid+"'"
                c.execute(s)
                d=c.fetchone()
                btime=d[0]
                import datetime
            
                # minute = 60
                # hours= 24
                # hours_added=datetime.timedelta(minutes=minute)
                # hours_added = datetime.timedelta(minutes=minute)

                # btime = btime + hours_added

                print(btime.now())
            s="insert into tblofferbooking(oid,cEmail,bdate,status) values('"+oid+"','"+email+"','"+bdate+"','booked')"
            c.execute(s)
            s="select max(obookid) from tblofferbooking"
            c.execute(s)
            d=c.fetchone()
            bookingid=d[0]
            # msg="Thank you for your booking. Booking details is Date: "+str(bdate)+" Time: "+str(btime)+" Booking No: "+str(bookingid)+"LCC EKM"
            # sendsms(contact,msg)
        elif btype=="treatment":
            s="select pEmail from tblcategory where catid in(select catid from tbltreatment where tId='"+oid+"')"
            c.execute(s)
            d=c.fetchone()
            pemail=d[0]
            s="select count(*) from tbltreatmentbooking where bdate='"+str(bdate)+"' and tId in(select tId from tbltreatment where catid in(select catid from tblcategory where pEmail='"+pemail+"'))"
            print(s)
            c.execute(s)
            d=c.fetchone()
            # btime="1:00 AM"
            # btime=request.POST['txtTime']
            if(d[0]>0):
                s="select max(tbId) from tbltreatmentbooking where bdate='"+bdate+"' and tId in(select tId from tbltreatment where catid in(select catid from tblcategory where pEmail='"+pemail+"'))"
                c.execute(s)
                d=c.fetchone()
                bid=d[0]
                s="select bTime from tbltreatmentbooking where tbId='"+str(bid)+"'"
                print(s)
                c.execute(s)
                d=c.fetchone()
                btime=d[0]
                import datetime
                
                # hours=24
                # hours_added=datetime.timedelta(hours=hours)
                # hours = 24
                minute=60
                hours_added = datetime.timedelta(minutes=minute)

                btime = btime + hours_added

                print(btime)
            s="insert into tbltreatmentbooking(tid,cEmail,bdate,status,btime) values('"+oid+"','"+email+"','"+str(bdate)+"','booked','"+str(btime)+"')"
            c.execute(s)
            s="select max(tbId) from tbltreatmentbooking"
            c.execute(s)
            d=c.fetchone()
            bookingid=d[0]
            # msg="Thank you for your booking. Booking details is Date: "+str(bdate)+" Time: "+str(btime)+" Booking No: "+str(bookingid)+"LCC EKM"
            # sendsms(contact,msg)
        elif btype=="package":
            s="select pEmail from tblpackage where packId='"+oid+"'"
            c.execute(s)
            d=c.fetchone()
            pemail=d[0]
            s="select count(*) from tblpackagebooking where bdate='"+bdate+"' and packId in(select packId from tblpackage where pEmail='"+pemail+"')"
            c.execute(s)
            d=c.fetchone()
            btime=request.POST['txtTime']
            # btime="1:00 AM"
            if(d[0]>0):
                s="select max(tbId) from tblpackagebooking where bdate='"+bdate+"' and packId in(select packId from tblpackage where pEmail='"+pemail+"')"
                c.execute(s)
                d=c.fetchone()
                bid=d[0]
                s="select bTime from tblpackagebooking where pbId='"+bid+"'"
                c.execute(s)
                d=c.fetchone()
                btime=d[0]
                import datetime
            
                minute = 20 
                # hours=24
                # hours_added=datetime.timezone(hours=hours)
                hours_added = datetime.timedelta(minutes=minute)

                btime = btime + hours_added

                print(btime)
            s="insert into tblpackagebooking(packId,cEmail,bdate,btime,status) values('"+oid+"','"+email+"','"+str(bdate)+"','"+str(btime)+"','booked')"
            c.execute(s)
            s="select max(pbId) from tblpackagebooking"
            c.execute(s)
            d=c.fetchone()
            bookingid=d[0]
            # msg="Thank you for your booking. Booking details is Date: "+str(bdate)+" Time: "+str(btime)+" Booking No: "+str(bookingid)+"LCC EKM"
            # sendsms(contact,msg)
        db.commit()
        return HttpResponseRedirect("/customerbooking")
    return render(request,"customerchoosedate.html")
def customerbooking(request):
    email=request.session['email']
    s="select tbloffer.oName,tblparlour.pName,tblofferbooking.bdate,tblofferbooking.btime from tbloffer,tblparlour,tblofferbooking where tbloffer.oId=tblofferbooking.oId and tbloffer.pEmail=tblparlour.pEmail and tblofferbooking.cEmail='"+email+"'"
    c.execute(s)
    offer=c.fetchall()
    s="select tblpackage.packName,tblparlour.pName,tblpackagebooking.bdate,tblpackagebooking.btime from tblpackage,tblparlour,tblpackagebooking where tblpackage.packId=tblpackagebooking.packId and tblpackage.pEmail=tblparlour.pEmail and tblpackagebooking.cEmail='"+email+"'"
    c.execute(s)
    package=c.fetchall()
    s="select tbltreatment.tName,tblparlour.pName,tbltreatmentbooking.bdate,tbltreatmentbooking.btime from tbltreatment,tblparlour,tbltreatmentbooking,tblcategory where tbltreatment.tId=tbltreatmentbooking.tId and tbltreatment.catid=tblcategory.catid and tblcategory.pEmail=tblparlour.pEmail and tbltreatmentbooking.cEmail='"+email+"'"
    c.execute(s)
    treatment=c.fetchall()
    return render(request,"customerbooking.html",{"offer":offer,"package":package,"treatment":treatment})
######################################################################
#                           LOAD PARLOURS FOR CUSTOMER
######################################################################
def customerparlour(request):
    email=request.session["email"]
    s="Select cDistrict from tblcustomer where cEmail='"+email+"'"
    c.execute(s)
    d=c.fetchone()
    dist=d[0]
    s="select * from tblparlour where pDistrict='"+dist+"'"
    c.execute(s)
    near=c.fetchall()
    s="select * from tblparlour where pDistrict<>'"+dist+"'"
    c.execute(s)
    far=c.fetchall()
    return render(request,"customerparlour.html",{"near":near,"far":far})
def customerparlourmore(request):
    pemail=request.GET.get("id")
    cemail=request.session['email']
    s="select * from tblparlour where pEmail='"+pemail+"'"
    c.execute(s)
    data=c.fetchall()
    s="select count(*) from tblcustomerreview where pEmail='"+pemail+"'"
    c.execute(s)
    dd=c.fetchone()
    rcount=dd[0]
    s="select count(*) from tblcustomerreview where pEmail='"+pemail+"' and cEmail='"+cemail+"'"
    c.execute(s)
    dd=c.fetchone()
    chance=dd[0]
    rating=0
    if rcount>0:
        s="select avg(rating) from tblcustomerreview where pEMail='"+pemail+"'"
        c.execute(s)
        d=c.fetchone()
        rating=d[0]
    return render (request,"customerparlourmore.html",{"email":pemail,"data":data,"rating":rating,"chance":chance})
def customertreatment(request):
    email=request.GET.get("id")
    s="select * from tbltreatment where catid in(select catid from tblcategory where pEmail='"+email+"') and status='1'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customertreatment.html",{"data":data})
def customerpackage(request):
    email=request.GET.get("id")
    s="select * from tblpackage where  pEmail='"+email+"' and status='1'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerpackage.html",{"data":data})
def customerpackagedetails(request):
    oid=request.GET.get("id")
    s="select tblpackage.*,tblparlour.* from tblpackage,tblparlour where tblpackage.pEmail=tblparlour.pEmail and tblpackage.packId='"+oid+"'"
    c.execute(s)
    offer=c.fetchall()
    s="select tName,tImg from tbltreatment where tId in(select tId from tblpackagetreatment where packId='"+oid+"')"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        return HttpResponseRedirect("/customerchoosedate?id="+str(oid)+"&type=package")
    return render(request,"customerpackagedetails.html",{"data":data,"offer":offer})
######################################################################
#                           LOAD RATING FOR CUSTOMER
######################################################################
def customerrate(request):
    msg=""
    rate=request.GET.get("rate")
    pemail=request.GET.get("pemail")
    cemail=request.session['email']
    if request.POST:
        feed=request.POST['txtfeedback']
        s="insert into tblcustomerreview(pEmail,cEmail,rDate,rating,review) values('"+pemail+"','"+cemail+"',(select sysdate()),'"+rate+"','"+feed+"')"
        c.execute(s)
        db.commit()
        msg="Review added"
    return render(request,"customerrate.html",{"rating":rate,"msg":msg})