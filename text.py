"""
- US income tax is calculated using a set of Tax Brackets.
- Tax Brackets define a set of income ranges and the tax rate for dollars in that range.
- The key feature is that higher income ranges can be taxed at a different (usually higher) rate without changing the tax rate on the earlier dollars.


Example Brackets:

| Income Range | Tax Rate |
|--------------|----------|
| [0, 50000]   | 5%       |
| >50000       | 10%      |


Naive Taxation:

tax(brackets, 50000) = 50000 * 0.05 = 2500
tax(brackets, 50001) = 50001 * 0.1 = 5000.1

Adding one dollar of income causes a huge jump!


Taxation with tax brackets:

tax(brackets, 50001) = 50000 * 0.05 + 1 * 0.1 = 2500.1

Much more fair!


A more complex set of brackets:

| Income Range    | Tax Rate |
|-----------------|----------|
| [0, 50000]      | 5%       |
| [50001, 80000]  | 10%      |
| (80000, 150000] | 15%      |
| >150000         | 20%      |


Write an implementation of a tax function in the language of your choice
- Parameters: A set of brackets (not hard coded, use whatever representation you prefer), Income
- Returns: Tax owed
- Constraints:
  - Brackets must cover all income ranges with no gaps and no overlap.
  - Incomes, tax rates, and bracket bounds must be non-negative
  """
  
# | [0, 50000]      | 5%       | 2500
# | (50000, 80000]  | 10%      | 2500 + (diff betwween v1 and v2 = 30000k tax at 10 % is  3000) = 5500
# | (80000, 150000] | 15%      | 5500 + (diff between v1 and v2 = 70000k tax at 15 % is  10500) = 16000
# | >150000         | 20%      | 160000 + 

# 50000 * 0.05 + 25000 * 0.10


'''

brackets = {
    [0, 50000] : 0.05
    [50001, 80000] : 0.10
    [80001, 100000] :0.15
    [100001, 150000] :0.18
    [150001, math.inf] : 0.20
}

input variable = x
tax_owed = 0
if x falls in ln 34
    do somelogic
    5% of x
elif x falls in ln 35
    build on stored percent
    diff between lower bracket and x 
    take amount and apply percentage 
    add percentage to the prior stored percent
elif x falls in ln 36
    build on stored percent
    diff between lower bracket and x 
    take amount and apply percentage 
    add percentage to the prior stored percent
elif x falls in ln 36
        build on stored percent
    diff between lower bracket and x 
    take amount and apply percentage 
    add percentage to the prior stored percent
else x falls in ln 37
    if x above 15000
    x times percentange
    
return tax_owed



for bracket in range(len(brackets)):
    if x in bra
    
    // logic 
    
'''


def tax_calculator(brackets:dict)
  
  
  
  