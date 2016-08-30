from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import VoterInfo
from .models import Citizenship
from .models import Address
from .models import Disability
from django.utils import timezone
from random import randint


def index(request):
    voter_list = VoterInfo.objects.all()
    
    context = {'voter_list': voter_list}
    
    return render(request, 'polls/index.html', context)
   

def edit(request):
    check=2
    if request.method=='POST':
      
      x=VoterInfo()
      try:
         vid=request.POST['voter_id']
         x=VoterInfo.objects.get(voter_id=vid)
         a=Address.objects.get(address_id=x.address_id)
         c=Citizenship.objects.get(citizenship_id=vid)
         try:
           d=Disability.objects.get(disability_id=x.disability_id)
         except:
           d=1   
         check=0
         

      except:
         check=1 
    return render(request, 'polls/edit.html',{'check':check,'x':x})


def edit2(request):
    
    check=2
    



    

    if request.method=='POST':
       check=0
       try:
          voter_id=request.POST['voter_id']
          #voter_id=90077      
       except:
          check=1

       name=request.POST['name']
       try:

         gender=request.POST['gender']
       except: 
         check=1

       spousename=request.POST['spousename']
       fathername=request.POST['fathername']
       gfathername=request.POST['gfathername']
       mothertongue=request.POST['mothertongue']
       mobile=request.POST['mobile']
       email=request.POST['email']
       try:

         literacystatus=request.POST['literacystatus']
       except:
         check=1
       qualification=request.POST['qualification']
       district=request.POST['district']
       vdc_municipality=request.POST['vdc_municipality']
       try:
          ward_no=request.POST['ward_no']
       except:
          check=1


       try:
          disability=request.POST['disability']
       except:
          check=1
       citizenship=request.POST['citizenship']
       cdistrict=request.POST['cdistrict']
       cvdc_municipality=request.POST['cvdc_municipality']
       cward_no=request.POST['cward_no']
       citizenshiptype=request.POST['citizenshiptype']
       birthdistrict=request.POST['birthdistrict']
       issuedate=request.POST['issuedate']
       dob=request.POST['dob']    
 
       if name== ''   or  fathername=='' or gfathername=='' or mothertongue=='' or district=='' or vdc_municipality=='' or citizenship=='' :
          check=1
       if cdistrict=='' or cvdc_municipality=='' or citizenshiptype=='' or birthdistrict=='' or issuedate=='' or dob=='':
          check=1


       if check==0 :      
             

             dis=request.POST['disability']
             try:
                dis=1
                d=Disability.objects.get(disability_id=dis)
             except:
                dis=0

             

            
          


             
             x=request.POST['district']
             y=request.POST['vdc_municipality']
             z=request.POST['ward_no']
             
             #  If Address previously does  not exist , create new
             try:
                a=Address.objects.get(district=x , vdc_municipality=y , wardno=z)
             except:
                tot=Address.objects.all()
                l=len(tot)
                a=Address.objects.create(address_id=l+1,district=x,vdc_municipality=y,wardno=z)
                a.save()
             a=Address.objects.get(district=x , vdc_municipality=y , wardno=z) 

             c=Citizenship()
             c.citizenship_id=citizenship
             
             c.citizenshiptype=citizenshiptype
             c.birthdistrict=birthdistrict
             c.issuedate=issuedate;
             c.dob=dob
             c.issuedaddress=a
             c.save()
             
             v=VoterInfo()
             
           
             
             

             v.name=name
             v.voter_id=voter_id
             v.citizenship=c
             v.gender=gender
             v.spousename=spousename
             v.fathername=fathername
             v.gfathername=gfathername
             v.mothertongue=mothertongue
             v.mobile=mobile
             v.email=email
             v.literacystatus=literacystatus
             v.qualification=qualification

             v.address=a
             if dis==1 :  
                v.disability=d
             
              
             v.save()
    

    return render(request, 'polls/edit2.html',{'check':check})

def voterview(request):
    check=2
    a=2
    c=3
    d=4 
    err=1
    x=VoterInfo()
    if request.method=='POST':
      try:
        vid=request.POST['citizenship_id']
        name=request.POST['name']
        x=VoterInfo.objects.get(citizenship=vid,name=name)
        
        a=Address.objects.get(address_id=x.address_id)
        c=Citizenship.objects.get(citizenship_id=vid)
        try:
          d=Disability.objects.get(disability_id=x.disability_id)
        except:
          d=1   
        check=0
      except:
        check=1   
    if check == 0:
      return render(request,'polls/viewvoter.html',{'check':check,'x':x,'a':a,'c':c,'d':d})
      
    else:
      err=2
      return render(request, 'polls/err.html',{'err':err})

def voteredit(request):
 
    check=2
    v=7 #random
    if request.method=='POST':
      try:
        vid=request.POST['voter_id']
        
        x=VoterInfo.objects.get(voter_id=vid)
        
        v=x.voter_id
        x.delete()
        check=0
      except:
        check=1
    
    return render(request,'polls/editvoter.html',{'v':v,'check':check})

def candid(request):

  if request.method == 'POST':
       
    canVoterId = request.POST['can_voter_id']
    moverVoterId = request.POST['mover_voter_id']
    suppVoterId = request.POST['supp_voter_id']
    
    canName = request.POST['can_name']
    canDob = request.POST['can_dob']
    canGender = request.POST['can_gender']
    canFatherName = request.POST['can_father_name']
    canParty = request.POST['can_party']

    if canParty == 'Yes':
      canPartyName = request.POST['can_party_name']
    	
      
      try:
        partyVal = Party.objects.get(party_name = canPartyName)

      except:
        partyId = randint(100000,999999)  #int(hashlib.md5(canPartyName).hexdigest(), 16) >> 64
        partyVal = Party.objects.create(party_id = partyId,
                    party_name = canPartyName)
        partyVal.save()

    else:
    	canPartyName = None
    	partyId = None

    canPledgeBank = request.POST['can_pledge_bank']
    canPledgeNo = request.POST['can_pledge_no']
    canDistrict = request.POST['can_district']
    canVDC = request.POST['can_vdc']
    canWard = request.POST['can_ward']
    canAreaDistrict = request.POST['can_area_district']
    canAreaNo = request.POST['can_area_no']

    moverName = request.POST['mover_name']
    moverDob = request.POST['mover_dob']
    moverGender = request.POST['mover_gender']
    moverFatherName = request.POST['mover_father_name']
    moverDistrict = request.POST['mover_district']
    moverVDC = request.POST['mover_vdc']
    moverWard = request.POST['mover_ward']

    suppName = request.POST['supp_name']
    suppDob = request.POST['supp_dob']
    suppGender = request.POST['supp_gender']
    suppFatherName = request.POST['supp_father_name']
    suppDistrict = request.POST['supp_district']
    suppVDC = request.POST['supp_vdc']
    suppWard = request.POST['supp_ward']

    #Generate a unique id based on the input parameters
    canId = randint(100000,999999)  #int(hashlib.md5(str(canVoterId)).hexdigest(), 16) >> 64
    moverId = randint(100000,999999) #int(hashlib.md5(str(moverVoterId)).hexdigest(), 16) >> 64
    suppId = randint(100000,999999)  #int(hashlib.md5(str(suppVoterId)).hexdigest(), 16) >> 64
    areaId = randint(100000,999999)  #int(hashlib.md5(canAreaDistrict + str(canAreaNo)).hexdigest(), 16) >> 649
  
    canAddressId = randint(100000,999999)#int(hashlib.md5(canDistrict + canVDC + str(canWard)).hexdigest(), 16) >> 64
    moverAddressId =randint(100000,999999) #int(hashlib.md5(moverDistrict + moverVDC + str(moverWard)).hexdigest(), 16) >> 64
    suppAddressId = randint(100000,999999)	 #int(hashlib.md5(suppDistrict + suppVDC + str(suppWard)).hexdigest(), 16) >> 64
      
    try:
      canAddress = Address.objects.get(district = canDistrict, 
            vdc_municipality = canVDC, wardno = canWard)
      moverAddress = Address.objects.get(district = moverDistrict, 
            vdc_municipality = moverVDC, wardno = moverWard)
      suppAddress = Address.objects.get(district = suppDistrict, 
            vdc_municipality = suppVDC, wardno = suppWard)
      areaVal = Area.objects.get(area_no = canAreaNo, 
            area_district = canAreaDistricts)

    except:
      
      canAddress =  Address.objects.create(address_id = canAddressId, 
            district = canDistrict, vdc_municipality = canVDC, 
            wardno = canWard)
      moverAddress = Address.objects.create(address_id = moverAddressId,
             district = moverDistrict, vdc_municipality = moverVDC, 
             wardno = moverWard)
      suppAddress = Address.objects.create(address_id = suppAddressId,
             district = suppDistrict, vdc_municipality = suppVDC, 
             wardno = suppWard)

      areaVal = Area.objects.create(area_id = areaId, area_no = canAreaNo,
             area_district = canAreaDistrict)

      canAddress.save()
      suppAddress.save()
      moverAddress.save()
      areaVal.save()


    #address = Address()
    #address.address_id = addressId
    #address.district = canDistrict
    #address.vdc_municipality = canVDC
    #address.wardno = canWard

    supporter = Supporter()
    supporter.supp_id = suppId
    supporter.supp_fullname = suppName
    supporter.supp_dob = suppDob
    supporter.supp_gender = suppGender
    supporter.supp_fathername = suppFatherName
    supporter.supp_voter_id = suppVoterId
    supporter.supp_address_id = suppAddressId
    supporter.save()

    mover = Mover()
    mover.mover_id = moverId
    mover.mover_fullname = moverName
    mover.mover_dob = moverDob
    mover.mover_gender = moverGender
    mover.mover_fathername = moverFatherName
    mover.mover_voter_id = moverVoterId
    mover.mover_address_id = moverAddressId
    mover.save()

    #area = Area()
    #area.area_d = areaId
    #area.area_no = canAreaNo
    #area.area_district = canAreaDistrict
    #area.save()

    candidate = Candidate()
    candidate.can_id = canId
    candidate.can_fullname = canName
    candidate.can_gender = canGender
    candidate.can_dob = canDob
    candidate.can_fathername = canFatherName
    candidate.can_date = str(datetime.date.today())
    candidate.can_address_id = canAddressId
    candidate.can_area_id = areaId
    candidate.can_party_id = partyId
    candidate.can_mover_id= moverId
    candidate.can_supp_id= suppId
    candidate.can_voter_id= canVoterId
    candidate.save()

    pledge = Pledge()
    pledge.pl_voucherno = canPledgeNo
    pledge.pl_bankname = canPledgeBank
    pledge.pl_can_id = canId
    pledge.save()


  return render(request, 'polls/candid.html')





def voter(request):
    
      
    

 





    check=2

    if request.method=='POST':
       check=0
       try:
          #voter_id=request.POST['voter_id']
          voter_id=randint(100000,999999) 
       except:
          check=1

       name=request.POST['name']
       try:

         gender=request.POST['gender']
       except: 
         check=1

       spousename=request.POST['spousename']
       fathername=request.POST['fathername']
       gfathername=request.POST['gfathername']
       mothertongue=request.POST['mothertongue']
       mobile=request.POST['mobile']
       email=request.POST['email']
       try:

         literacystatus=request.POST['literacystatus']
       except:
         check=1
       qualification=request.POST['qualification']
       district=request.POST['district']
       vdc_municipality=request.POST['vdc_municipality']
       try:
          ward_no=request.POST['ward_no']
       except:
          check=1


       try:
          disability=request.POST['disability']
       except:
          check=1
       citizenship=request.POST['citizenship']
       cdistrict=request.POST['cdistrict']
       cvdc_municipality=request.POST['cvdc_municipality']
       cward_no=request.POST['cward_no']
       citizenshiptype=request.POST['citizenshiptype']
       birthdistrict=request.POST['birthdistrict']
       issuedate=request.POST['issuedate']
       dob=request.POST['dob']    
 
       if name== ''   or  fathername=='' or gfathername=='' or mothertongue=='' or district=='' or vdc_municipality=='' or citizenship=='' :
          check=1
       if cdistrict=='' or cvdc_municipality=='' or citizenshiptype=='' or birthdistrict=='' or issuedate=='' or dob=='':
          check=1


       if check==0 :      
             

             dis=request.POST['disability']
             try:
                dis=1
                d=Disability.objects.get(disability_id=dis)
             except:
                dis=0

             

            
          


             
             x=request.POST['district']
             y=request.POST['vdc_municipality']
             z=request.POST['ward_no']
             
             #  If Address previously does  not exist , create new
             try:
                a=Address.objects.get(district=x , vdc_municipality=y , wardno=z)
             except:
                tot=Address.objects.all()
                l=len(tot)
                a=Address.objects.create(address_id=l+1,district=x,vdc_municipality=y,wardno=z)
                a.save()
             a=Address.objects.get(district=x , vdc_municipality=y , wardno=z) 

             c=Citizenship()
             c.citizenship_id=citizenship
             
             c.citizenshiptype=citizenshiptype
             c.birthdistrict=birthdistrict
             c.issuedate=issuedate;
             c.dob=dob
             c.issuedaddress=a
             c.save()
             
             v=VoterInfo()
             
           
             
             

             v.name=name
             v.voter_id=voter_id
             v.citizenship=c
             v.gender=gender
             v.spousename=spousename
             v.fathername=fathername
             v.gfathername=gfathername
             v.mothertongue=mothertongue
             v.mobile=mobile
             v.email=email
             v.literacystatus=literacystatus
             v.qualification=qualification

             v.address=a
             if dis==1 :  
                v.disability=d
             
              
             v.save()

    print('check')
    print(check) 
    return render(request, 'polls/voter.html',{'check':check})




