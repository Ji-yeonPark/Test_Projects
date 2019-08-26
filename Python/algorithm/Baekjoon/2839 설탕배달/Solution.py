sugar = int(input())
package = 0

while sugar > 0:
    if sugar % 5 == 0:
        package = package + (sugar / 5)
        break
    sugar -= 3
    package += 1

    if sugar < 0:
        package = -1

print package
