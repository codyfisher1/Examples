from StatCollect import Correlation_Coef
def ElementSelection(Array,Array_Number):
    
    ElementSelection.ElementList = []
    
    for p in Array:
        Stat = p[Array_Number]
        ElementSelection.ElementList.extend([Stat])

        SelectExcept = p.pop(Array_Number)
        #SelectExceptFront = p[:Array_Number]
        #Array_Number_After = Array_Number +1
        #SelectExceptBack = p[(Array_Number_After):]
        #SelectExcept = SelectExceptBack + SelectExceptFront
    ElementSelection.ExclusionList = Array



def ElementCompare(Array):
    ElementCompare.ElementList = []
    length = range(42)
    for q in length:
        
    
        ElementSelection(Array,q)
        Primary_List = ElementSelection.ElementList
        SecondaryList = ElementSelection.ExclusionList
        print(Primary_List)
        print(SecondaryList)
    
        for r in range(len(SecondaryList)):
            Correlation_Coef(Primary_List,SecondaryList[r])
            r_value = Correlation_Coef.r_array
            ElementCompare.ElementList.extend(r_value)

        
