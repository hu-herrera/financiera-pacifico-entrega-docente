"""Verify the delivered bytes, archive and economic controls; no external packages."""
from pathlib import Path
import hashlib,zipfile,json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
rows=[line.split(maxsplit=1) for line in (R/'MANIFIESTO.sha256').read_text().splitlines() if line.strip()]
for digest,name in rows:
 p=R/name;assert p.is_file(),name
 assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,('manifest',name)
with zipfile.ZipFile(R/'Entrega_Profesor_Financiera_Pacifico.zip') as z:
 assert z.testzip() is None
 assert set(z.namelist())=={name for _,name in rows}|{'MANIFIESTO.sha256'}
 for _,name in rows:assert z.read(name)==(R/name).read_bytes(),('archive',name)
 assert z.read('MANIFIESTO.sha256')==(R/'MANIFIESTO.sha256').read_bytes()
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(R/'Anexos/Presupuesto_Inventario.xlsx') as z:
 root=ET.fromstring(z.read('xl/worksheets/sheet1.xml'));cells={c.get('r'):c for c in root.findall('.//s:c',ns)}
 for cell,value in {'B8':793126897,'C8':281194478,'B9':660607380,'C9':660607380,'B11':1503734277,'C11':966801858,'B19':11010123,'C19':11010123}.items():assert round(float(cells[cell].find('s:v',ns).text))==value,(cell,value)
 for name in z.namelist():
  if name.startswith('xl/worksheets/') and name.endswith('.xml'):assert not [c for c in ET.fromstring(z.read(name)).findall('.//s:c',ns) if c.get('t')=='e']
annual=11010123*12
assert 793126897+annual+10000000==935248373
assert 281194478+annual+5000000==418315954
assert 935248373+4*(annual+10000000)==1503734277
assert 418315954+4*(annual+5000000)==966801858
for p in (R/'Fuentes').glob('*.md'):
 text=p.read_text();assert 'github.io/fin/' not in text,p
 assert 'https://github.com/hu-herrera/financiera-pacifico-trabajo-privado/' not in text,p
print(json.dumps({'scope':'DOCUMENTOS_Y_PAQUETE','manifest_entries':len(rows),'archive':'PASS','workbook':'PASS','annual_economics':'PASS','public_links':'PASS'},ensure_ascii=False))
