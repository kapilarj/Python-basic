import Module as m
m.fn()
print(m.version)

if __name__ == '__main__':
    print(__name__)
    print("main")
else:
    print("noo")

print(dir(m))