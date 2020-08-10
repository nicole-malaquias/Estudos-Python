from Cpf_Cnpj import Documento
from Cpf_Cnpj import DocCnpj
from Cpf_Cnpj import DocCpf



from validate_docbr import CPF
from validate_docbr import CNPJ

#cpf= CPF()
#print(cpf.validate("012.345.678-90")) #verdadeiro
#cpf2= Cpf("15316264754")
#print(cpf2)


exemploCnpj= "35379838000112"
documentoCnpj = Documento.cria_documento(exemploCnpj)
print(documentoCnpj)

exemploCpf = "41525972839"
documentoCpf = CpfCpnj(exemploCpf,"cpf")
print(documentoCpf)


cpf= "41525972839"
docume=nto = documento.cria_documento(cpf)
print(documento)










