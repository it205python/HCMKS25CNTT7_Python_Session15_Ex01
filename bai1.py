inventory_stock = 100
total_revenue = 0.0

def add_stock(amount):
    """
    Cập nhật số lượng hàng vào kho.
    Args:
        amount (int): Số lượng hàng muốn thêm vào.
    """
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}.")

def validate_number(quantity, price):
    """kiểm tra đầu vào"""
    if (not quantity.isdigit() or not price.isdigit()):
        print("Dữ liệu nhập vào phải là số")
        return False

    if (int(quantity) <= 0 or int(price) <= 0):
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return False

    return True

def process_sale(quantity):
    """kiểm kho và xử lý bán hàng"""
    global inventory_stock
    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return False
    return True

def calculate_final_price(quantity, price):
    """tính chi phí"""
    discount = 0
    total_money = quantity * price

    if (total_money >= 1000):
        discount = total_money * 0.1

    after_dsc = total_money - discount
    vat = after_dsc * 0.08
    final_total = after_dsc + vat

    return total_money, discount, vat, final_total

def print_report():
    """
    hiển thị báo cáo 
    global
        inventory_stock (int): số lượng sản phẩm còn lại trong kho
        total_revenue (float): tổng doanh thu thu được từ tất cả các đơn hàng thành công
    """
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")

def main():
    global inventory_stock
    global total_revenue
    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                print("--- NHẬP HÀNG ---")
                while True:
                    add_quantity = input("Nhập số lượng sản phẩm muốn thêm: ")

                    if add_quantity.isdigit():
                        amount = int(add_quantity)

                        if amount > 0:
                            add_stock(amount)
                            break
                        else:
                            print("Lỗi: Dữ liệu nhập vào phải lớn hơn 0.")
                    else:
                        print("Lỗi: Vui lòng không nhập chữ và ký tự đặc biệt.")

            case "2":
                print("--- BÁN HÀNG ---")
                quantity = input("Nhập số lượng mua: ")
                price = input("Nhập đơn giá ($): ")

                if (not validate_number(quantity, price)):
                    continue

                quantity = int(quantity)
                price = float(price)

                if (not process_sale(quantity)):
                    continue

                total_money, discount, vat, final_total = calculate_final_price(quantity, price)
                inventory_stock -= quantity
                total_revenue += final_total
                print("-> Hóa đơn chi tiết:")
                print(f"Số lượng: {quantity:<10} | Đơn giá: ${price:.1f}")
                print(f"Tạm tính: {total_money}")
                print(f"Giảm giá (10%): ${discount}")
                print(f"Thuế VAT (8%): ${vat}")
                print(f"Tổng thanh toán: ${final_total}")
                print(f"Đã bán thành công!")

            case "3":
                print_report()

            case "4":
                print("Cảm ơn bạn đã sử dụng hệ thống. Thoát chương trình...")
                break

            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại (1-4).")

main()