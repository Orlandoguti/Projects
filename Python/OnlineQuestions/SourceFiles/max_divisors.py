
list_value = []


def get_value():
    for i in range(0, 20):
        list_value.append(int(input()))
    return list_value


def divisor(n):
    for k in range(n):
        x = len([k for k in range(1, n+1) if not n % k])
    return x


list_values = get_value()
divisor_list = []

for i in range(0, 20):
    divisor_list.append(divisor(list_values[i]))
    # print(list_value[i], divisor_list[i])


# print(divisor_list)
Max_divisor = max(divisor_list)
# print("max div", Max_divisor)
index_Max_divisor = divisor_list.index(Max_divisor)
# print("max DIv index", index_Max_divisor)
Max_value = list_values[index_Max_divisor]
# print("max Value", Max_value)
out_max_value = 0
out_max_divisor = 0

for i in range(0, len(divisor_list)-1):
    if divisor_list[i] >= Max_divisor and list_values[i] >= Max_value:
        out_max_divisor = divisor_list[i]
        out_max_value = list_values[i]

print(out_max_value, out_max_divisor)
