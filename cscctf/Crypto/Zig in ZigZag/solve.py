flag = "WbiushCTneoebFppelpAHiaodMdtilaelehsasnDOashnegrcmeTvKYeftAoddZIoWrheiocQhndHSismhIeTnuiuemAaopNeesCodFpesalvHpoTrUoDOihettgeeitoesmefndriioTrnTTZepcPrOTocroegohideipouhnsiBIToigAtihbtiWMteshHsZndtelHshehCTeaPagYoreoKetmohZrroCorTmwirhMmeid"

key = 16
arr = [["0" for i in range(len(flag)/key)] for j in range(key)]
row = 0
col = 0
count = 0
for i in range(len(flag)):
	arr[row][col] = flag[i]
	row = (row+1)%key
	col = (col+1)%(len(flag)/key)

for i in range(len(arr)):
    print ''.join(arr[i])