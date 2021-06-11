# %%
a="some"
print(id(a))
print(id("some"+"_"+"string"))
# %%
a='wtf'
b='wtf'
print(a is b)

a='wtf!'
b='wtf!'
print(a is b)

a, b ='wtf!', 'wtf!'
print(a is b)

# %%
print('a'*20 == 'aaaaaaaaaaaaaaaaaaaa')
print('a'*21 == 'aaaaaaaaaaaaaaaaaaaaa')

# %%
