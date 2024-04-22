with open("csudh.txt", encoding="utf-8") as f:
    d = f.read().split("\n")[1:]
    d = [x.split(";") for x in d]

print(f"3. feladat: Domainek száma: {len(d)}")

def domain(lv, domain):
    if lv <= len(domain.split(".")):
        return domain.split(".")[-lv]
    return "nincs"

print(f"5. feladat: A első domain felépítése:")
for i in range(1,6):
    print(f"\t{i}. szint: {domain(i, d[0][0])}")
print(d)
with open("table.html", "w", encoding="utf-8") as f:
    f.write("<table>\n")
    f.write("\t<tr>\n")
    f.write("\t\t<th>Domain</th>\n")
    f.write("\t\t<th>IP Address</th>\n")
    f.write("\t</tr>\n")
    for domain, ip in d:
        f.write("\t<tr>\n")
        f.write(f"\t\t<td>{domain}</td>\n")
        f.write(f"\t\t<td>{ip}</td>\n")
        f.write("\t</tr>\n")
    f.write("</table>\n")