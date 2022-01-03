
import name_genie

#titles_common_male=['master','mr','yeoman','old','young','His Honour']
#titles_common_female=['mistress','mrs','miss','mz','ms','goodie','old','young','Her Honour','madam']
#titles_royal_male=['Sir','king','lord','baron','duke','count','baronet']
#titles_royal_female=['lady','queen','madamme','Duchess', 'dame','baroness', 'countess']


# You can print directly
for i in range(15):
    print(name_genie.Generate_name("Troll",1,1,.9,('Bar','Gor','Rog'),1,False,False,nomen=True))
    print(name_genie.Generate_name("Ogre",syllables_max=3,nomen_suffix_list=("son",'dottr'),nomen_suffix_ratio=1))
    
# Or you can create an object and use it later
monster1=name_genie.Generate_name('BurghGnome',2,4,nomen_prefix_list=('Von','Of '),nomen_prefix_ratio=.3,title_ratio=1,title_list=("Dr.",'Mr','Mr','Mr','Mr'),cognomen_list=('The butcher','The baker', 'The candlestick maker'))
monster2=name_genie.Generate_name('Beastperson',4,9,1,cognomen_list=("Gutstomper","FleshRender","Skullbonker"))
print(monster1.values())

print(name_genie.Generate_name("",1,2)['praenomen'].title())

print("###########testing##########")
#quickname uses default arguments except syllable_min=2,syllable_max=4
monster3name=(name_genie.quickname())
print(monster3name)
##Both work
print(name_genie.quickname())


