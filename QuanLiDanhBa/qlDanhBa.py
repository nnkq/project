'''
Quản lý danh bạ
* các chức năng:
    - thêm liên hệ mới
    - xem danh sách liên hệ
    - tìm kiếm liên hệ theo tên or số điện thoại
    - xóa liên hệ
    - sửa thông tin liên hệ
    - lưu danh bạ vào file
    - đọc danh bạ từ file
'''

import json
import os

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = []
        self.load_contacts()
    
    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.contacts = [Contact(**item) for item in data]
        else:
            self.contacts = []
            
    def save_contacts(self):
        with open(self.filename, "w") as file:
            data = [{'name' : c.name, 'phone': c.phone,
                     'email': c.email, 'address': c.address} for c in self.contacts]
            json.dump(data, file, indent=4)
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Đã thêm liên hệ mới: {contact.name}")
        
    def display_contacts(self):
        if not self.contacts:
            print("Danh bạ rỗng.")
            return
        print("\n--- DANH BẠ ---")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name} - {contact.phone} - {contact.email} - {contact.address}")
        
    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if (keyword.lower() in contact.name.lower() or
                keyword in contact.phone):
                results.append(contact)
        
        if not results:
            print("Không tìm thấy liên hệ nào.")
        else:
            print("\n--- KẾT QUẢ TÌM KIẾM ---")
            for i, contact in enumerate(results, start=1):
                print(f"{i}. {contact.name} - {contact.phone} - {contact.email} - {contact.address}")
                
    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts[i] = new_contact
                self.save_contacts()
                print(f"Đã cập nhật liên hệ: {new_contact.name}")
                return
        print("Không tìm thấy liên hệ để cập nhật.")
        
    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                self.save_contacts()
                print(f"Đã xóa liên hệ: {name}")
                return
        print("Không tìm thấy liên hệ để xóa.")
        
def main():
    manager = ContactManager()
    
    while True:
        print("\n--- QUẢN LÝ DANH BẠ ---")
        print("1. Thêm liên hệ mới")
        print("2. Xem danh sách liên hệ")
        print("3. Tìm kiếm liên hệ")
        print("4. Cập nhật liên hệ")
        print("5. Xóa liên hệ")
        print("6. Thoát")
        
        choice = input("Chọn chức năng (1-6): ")
        
        if choice == '1':
            name = input("Nhập tên: ")
            phone = input("Nhập số điện thoại: ")
            email = input("Nhập email: ")
            address = input("Nhập địa chỉ: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
            
        elif choice == '2':
            manager.display_contacts()
            
        elif choice == '3':
            keyword = input("Nhập tên hoặc số điện thoại để tìm kiếm: ")
            manager.search_contact(keyword)
            
        elif choice == '4':
            name = input("Nhập tên liên hệ cần cập nhật: ")
            new_name = input("Nhập tên mới: ")
            new_phone = input("Nhập số điện thoại mới: ")
            new_email = input("Nhập email mới: ")
            new_address = input("Nhập địa chỉ mới: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            manager.update_contact(name, new_contact)
            
        elif choice == '5':
            name = input("Nhập tên liên hệ cần xóa: ")
            manager.delete_contact(name)
            
        elif choice == '6':
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

if __name__ == "__main__":
    main()