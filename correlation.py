import xml.etree.ElementTree as ET
tree = ET.parse('PostHistory.xml')
root = tree.getroot()

def search(list, platform):
    for i in list:
        if i == platform:
            return True
    return False
    
d=[]
a={}        
          
for i in range(0,len(root)):
	x=dict(root[i].attrib)
	try:
		if x['UserId']!='-1' and x['PostHistoryTypeId']=='2':	
			d.append(x['UserId'])
		else:
			pass	
	except:
		pass
		
			
for word in d:

        if search(a,word) == True:
            a[word] =a[word]+1
        if search(a,word) ==  False:
            a[word] = 1
            
tree1 = ET.parse('Users.xml')
root1 = tree1.getroot()
b={}
for i in range(0,len(root1)):
	x=dict(root1[i].attrib)
	b[x['Id']]=x['Reputation']
	
	

c=set(a.keys())

ac=[]
rep=[]
for i in c:
	if i in b.keys():
		ac.append(int(a[i]))
		rep.append(int(b[i]))
	

from scipy.stats import pearsonr
corr, _ = pearsonr(ac, rep)
print(corr)	
		
		
