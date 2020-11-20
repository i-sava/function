def key_of_max_value(dt=dict()):
  values = list(dt.values()) #[]
  print(values)
  if not values:
    return 'Не передано значень'
  M_value = max(values)#5
  for k, v in dt.items():
    if v == M_value:
      return k,v


def myfunc(a=0,b=0):
  return a if a>=b else b