import marmot

marmot.connect('localhost', 15685)

ds = marmot.get_dataset('POI/주유소_가격')
print(ds)
print(ds.record_count)
print(ds.bounds)
# for ds in marmot.get_dataset_all():
#     print(ds)
# for ds in marmot.get_dataset_all_in_dir('구역', True):
#     print(ds)
# for dir in marmot.get_dir_all():
#     print(dir)
# for dir in marmot.get_sub_dir_all('/교통', True):
#     print(dir)

for rec in ds.read():
    print(rec)

marmot.disconnect()