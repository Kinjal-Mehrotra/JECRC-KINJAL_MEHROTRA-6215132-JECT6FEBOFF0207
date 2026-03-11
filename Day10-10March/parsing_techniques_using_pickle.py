
import pickle
file=open('temp.txt','ab+')
data={
    'fullname':'ABC',
    'userid':'845413146',
    'password':'***'
}
print(f'Orignal data: {data}')
print(f'Type of orignal data:{type(data)}')

enc_data=pickle.dumps(data)

print(f'Encrypted data: {enc_data}')
print(f'Type of encrypted data:{type(enc_data)}')


dec_data=pickle.loads(enc_data)

print(f'Decrypted data: {enc_data}')
print(f'Type of Decrypted data:{type(dec_data)}')
file.write(enc_data)
file.seek(0)
enc_data_2=file.read()
print(type(enc_data_2))

ori_data=file.read()
print(type(ori_data))

print(file.read())
file.close()


