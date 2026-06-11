information_book = [
    {"id":"BK001", "room":"Phòng thảo luận A", "department":"Phòng markerting", "start_time":9 , "end_time":12, "total_duration":3, "time_classification": "Tiêu chuẩn"}

]

def display_booking(book):
    if len(book) == 0:
        print("Danh sách lịch đặt hiện đang trống!")
    else:
        for item in book:
            print(f"Mã BK: {item['id']:<3} | Tên phòng: {item['room']:<20}| Người đặt/phòng ban: {item['department']:<15} | Giờ bắt đầu: {item['start_time']:<3}| Giờ kết thúc: {item['end_time']:<3} | Thời lượng: {item['total_duration']} | Phân loại: {item['time_classification']}")

def delivier_time_classification(duration):
    if duration < 2:
        return "Ngắn"
    elif duration < 4:
        return "Tiêu chuẩn"
    elif duration < 6:
        return "Dài"
    else:
        return "Quá tải(Cần xem xét lại)"

def duplicate_bk(id_bk):
    for item in information_book:
        if item['id'] == id_bk:
            print("Mã BK này đã được đặt rồi")
            return True
    return None

def register_booking():
    while True:
        book_id = input("Nhập vào mã BK: ").strip().upper()
        if book_id == "":
            print("Mã lượt đặt không được để trống!")
            continue
        if duplicate_bk(book_id):
            continue
        break
    while True:
        name_room = input("Nhập vào tên phòng: ")
        if name_room == "":
            print("Tên phòng họp không được để trống!")
            continue
        break
    while True:
        name_register = input("Nhập vào tên người đặt: ")
        if name_register == "":
            print("Tên người đặt không được để trống!")
            continue
        break
    while True:
        try:
            time_start = input("Nhập giờ bắt đầu: ")
            time_end = input("Nhập vào giờ kết thúc: ")
            if time_start == "" or time_end == "":
                print("Giờ không được để trống!")
                continue
            time_start = int(time_start)
            time_end = int(time_end)
            if not (time_start >= 0 and time_start <= 24) and (time_end >= 0 and time_end <= 24 ):
                print("Giờ bắt đầu và giờ kết thúc phải nằm trong khoảng(0-24)")
                continue
            elif not time_end > time_start:
                print("Giờ kết thúc phải lớn hơn giờ bắt đầu!")
                continue
            break
        except ValueError:
            print("Giờ nhập không hợp lệ!Nhập lại!")
            continue
    total_duration = time_end - time_start
    delivier_classification = delivier_time_classification(total_duration)
    new_booking = { "id":book_id, "room": name_room, "department":name_register.title(), "start_time":time_start , "end_time":time_end, "total_duration":total_duration, "time_classification": delivier_classification}
    information_book.append(new_booking)

while True:
    menu_title = "HỆ THỐNG QUẢN LÝ PHÒNG HỌP - ĐẶT LỊCH HẸN ".center(60,"=")
    user_choice = input(f"""
{"=" * len(menu_title)}
{menu_title}
{"=" * len(menu_title)}
1. Hiển thị danh sách lịch đặt.
2. Đăng ký lịch đặt phòng mới.
3. Cập nhật thông tin lịch hẹn.
4. Hủy/Xóa lịch đặt phòng.
5. Tìm kiếm lịch đặt phòng.
6. Thống kê mật độ sử dụng.
7. Phân loại khung giờ tự động.
8. Thoát chương trình.
{"=" * len(menu_title)}
Nhập lựa chọn(1-8):  """)
    match user_choice:
        case "1":
            display_booking(information_book)
        case "2":
            register_booking()
        case "3":
            found = -1
            update_time = input("Nhập mã BK cần cập nhật: ").strip().upper()
            for i  in range(len(information_book)):
                if information_book[i]['id'] == update_time:
                    try:
                        update_time_start = input("Nhập giờ bắt đầu: ")
                        update_time_end = input("Nhập vào giờ kết thúc: ")
                        if update_time_start == "" or update_time_end == "":
                            print("Giờ không được để trống!")
                        update_time_start = int(update_time_start)
                        update_time_end = int(update_time_end)
                        if not (update_time_start >= 0 and update_time_start <= 24) and (update_time_end >= 0 and update_time_end <= 24 ):
                            print("Giờ bắt đầu và giờ kết thúc phải nằm trong khoảng(0-24)")
                        elif not update_time_end > update_time_start:
                            print("Giờ kết thúc phải lớn hơn giờ bắt đầu!")
                        found = i
                    except ValueError:
                        print("Giờ nhập không hợp lệ!")
            if found == -1:
                print("Không tìm thấy Mã BK phù hợp!")
            else:
                update_total_duration = update_time_end - update_time_start
                delivier_classification = delivier_time_classification(update_total_duration)
                information_book[found]['start_time'] = update_time_start
                information_book[found]['end_time'] = update_time_end
                information_book[found]['total_duration'] = update_total_duration
                information_book[found]['time_classification'] = delivier_classification
        case "4":
            delete_id_bk = input("Nhập vào mã BK cần giải phóng: ").strip().upper()
            found = True
            for i in range(len(information_book)):
                if information_book[i]['id'] == delete_id_bk:
                    delete_choice = input("Bạn có chắc muốn xóa lịch đặt phòng này không(Y/N): ").lower()
                    if delete_choice == "y":
                        information_book.pop(i)
                    found = False
                    print("Đã xóa thành công!")
                    break
            if found:
                print("Không tìm thấy mã BK này!")
        case "5":
            pass
        case "6":
            pass
        case "7":
            delivier_classification()
        case "8":
            print("Kết thúc chương trình!")
            print("[Tạm biệt]!")
            break
        case _:
            print("Hệ thống không có chức năng này!")