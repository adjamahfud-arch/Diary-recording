def isi_ctt():
    while True:
       try:
         catat =str(input("tulis catatan:")).title()
         if catat =="":
            print("catatan mohon di isi")
            continue
           
         if len(catat) >= 115:
            print("catatan sudah mencapai batas")
            continue
           
         return catat
       except ValueError:
           print("terjadi kesahan input")
           continue

       except Exception as wx:
           print(f"error:{wx}")
           continue

def tampil():
    while True:
       try:
         show =str(input("mau tampilkan data? YA/TiDAK:")).strip().lower()
         if show =="":
            print("harus di isi!")
            continue

         if not show.isalpha():
            print("harus di isi dengan angka")
            continue

         if not show in ["ya","tidak"]:
            print("pilihan hanya boleh di isi dengan ya dan tidak")
            continue
         return show
         
       except ValueError:
           print("eror angka")
           continue
         
       except Exception as ecx:
           print(f"error {ecx}")
         
def id_input():
    while True:
       try:
         has_id =input("masukan id:").strip()
         if has_id =="":
            print("harus di isi!")
            continue
           
         if has_id.isalpha():
            print("pilihan harus di di dengan angka!")
            continue
         is_id =int(has_id)
         return is_id
         
       except ValueError:
           print("program mengalami error")
           continue
         
       except Exception as epc:
           print(f"error:{epc}")
         
if __name__ =="__main__":
   id_input()
  
  