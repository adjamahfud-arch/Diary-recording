import json
import logging
from pathlib import Path

file =Path("data/data_proyek.json")

logging.basicConfig(
     filename="Program.log",
     level=logging.INFO,
     format="%(levelname)s - %(message)s"
)

class Data:
    def __init__(self,id :int, catatan: str, waktu: str) -> None:
        self.id =id
        self.catatan =catatan
        self.waktu =waktu
        self.status =True
    
    def to_dict(self) -> dict:
        return {
           "id": self.id,
           "catatan": self.catatan,
           "waktu": self.waktu,
           "status": self.status
        }
      
    @classmethod
    def from_dict(cls,data):
        dtai =cls(data["id"],data["catatan"],data["waktu"])
        dtai.status =data["status"]
        return dtai
      
    @classmethod
    def load_file(cls):
        try:
          hisfile =json.loads(
             file.read_text(encoding="utf-8")
          )
          return [cls.from_dict(x) for x in hisfile]
          
        except FileNotFoundError:
             logging.exception("file tidak di temukan")
             return []
          
        except (json.JSONDecodeError, KeyError) as al:
             logging.exception("file rusak")
             print(f"file rusak ({al})")
             return []
          
        except Exception as ex:
             logging.exception("error")
             print(f"error:{ex}")
             return []
          
    @staticmethod
    def simpan(data):
        try:
          data_se =[y.to_dict() for y in data]
          file.write_text(
              json.dumps(data_se, ensure_ascii=False, indent=4),
              encoding="utf-8"
          )
          return True
        except OSError as es:
             logging.exception("error")
             print(f"error:{es}")
             return False
          
        except Exception as ex:
             logging.exception("eroorc")
             print(f"error:{ex}")
             return False
              
       
            