from datetime import datetime
from storage import Data
import validation as vl

format_waktu: str ="%H:%M %d %A %Y"

class Mainframe:
    def __init__(self) -> None:
        self.data_center =Data.load_file()
        
      
    def tambah(self,tambah_dta):
        self.data_center.append(tambah_dta)

    def isian(self,ctt: str, waktu: str) -> None:
         ever =self.ubah(ctt)
         ps_key =ever * 3
         user_is =Data(ps_key,ctt,waktu)
         self.tambah(user_is)
         starus =Data.simpan(self.data_center)
         if starus:
            print(f"id {ps_key}")
            print("data berhasil simpan")
           
    @staticmethod
    def ubah(data: str) -> int:
        change =len(data)
        return change
      
    def tampilkan(self,id: int) -> None:
        nomor = 0
        if not self.data_center:
           print("dat masih kosong")
           return
        for l , urut in enumerate(self.data_center, start=1):
            if urut.id ==id:
               print(f"{l}.{urut.catatan}")
               nomor += 1
        if nomor == 0:
           print("data tidak di temukan")
          
    def sub_tampil(self,pilih: str) -> None:
        if pilih =="ya":
           i_id =vl.id_input()
           self.tampilkan(i_id)
           print("terimakasih:)")
      
class Time:
    @staticmethod
    def waktu() -> str:
        jam =datetime.now().strftime(format_waktu)
        return jam
      
def main():
    mf =Mainframe()
    wk =Time()
    iscatat =vl.isi_ctt()
    timl =wk.waktu()
    mf.isian(iscatat,timl)
    is_show =vl.tampil()
    mf.sub_tampil(is_show)
  
  
          

if __name__ =="__main__":
   main()
    