# Odoo Fruit ERP Custom Addons

Repository này chứa các custom module Odoo được phát triển cho đồ án triển khai ERP trong doanh nghiệp thu mua, phân phối và bán lẻ trái cây tươi.

Các module được xây dựng nhằm mở rộng các luồng nghiệp vụ chuẩn của Odoo như Inventory, CRM, Sales và Pricing để phù hợp hơn với đặc thù ngành trái cây tươi, bao gồm:

- Quản lý Lot/Batch và truy xuất nguồn gốc.
- Kiểm định chất lượng hàng nhập kho.
- Ghi nhận hàng hư, hàng lỗi, hao hụt.
- Kiểm soát xuất kho theo nguyên tắc FEFO.
- Gợi ý lô hàng nên xuất trước.
- Tổng hợp báo cáo đóng ngày.
- Thu thập tín hiệu thị trường từ CRM.
- Tạo bảng giá trái cây hằng ngày cho Sales.

---

## 1. Bối cảnh dự án

Dự án mô phỏng việc triển khai Odoo ERP cho một doanh nghiệp kinh doanh trái cây tươi, có các hoạt động chính:

- Thu mua trái cây từ nhà vườn, hợp tác xã và nhà cung cấp.
- Kiểm định chất lượng đầu vào.
- Quản lý tồn kho theo lô hàng, hạn sử dụng và vị trí kho.
- Phân phối cho khách sỉ, siêu thị, cửa hàng bán lẻ và kênh online.
- Theo dõi cơ hội bán hàng trong CRM.
- Tạo báo giá, đơn bán hàng và bảng giá theo ngày.
- Ghi nhận hao hụt, hàng hư và báo cáo vận hành.

Do trái cây là nhóm hàng có vòng đời ngắn, doanh nghiệp cần kiểm soát chặt chẽ chất lượng, hạn sử dụng và biến động giá bán theo thị trường. Vì vậy, các module trong repository này được xây dựng để bổ sung những nghiệp vụ đặc thù mà Odoo Community/Standard chưa đáp ứng đầy đủ trong phạm vi đồ án.

---

## 2. Vấn đề nghiệp vụ cần giải quyết

Doanh nghiệp trái cây tươi thường gặp các vấn đề sau:

| Vấn đề | Tác động |
|---|---|
| Trái cây có hạn sử dụng ngắn | Dễ phát sinh hư hỏng, hao hụt nếu không xuất kho đúng thứ tự |
| Hàng nhập cần kiểm định chất lượng | Cần tách hàng đạt, hàng lỗi, hàng trả nhà cung cấp hoặc hàng hủy |
| Thiếu truy xuất nguồn gốc theo lô | Khó biết hàng đến từ nhà vườn nào, ngày thu hoạch nào |
| Hàng hư/hỏng chưa được ghi nhận rõ | Khó tính chi phí hao hụt và đánh giá hiệu quả vận hành |
| Giá bán thay đổi theo ngày | Sales cần bảng giá cập nhật dựa trên nhu cầu thị trường |
| CRM chưa hỗ trợ ra quyết định giá | Thông tin khách hỏi, giá đối thủ, nhu cầu thị trường chưa được tổng hợp thành bảng giá |
| Các module chưa liên kết đủ sâu | Cần kết nối CRM, Sales, Inventory và báo cáo quản trị thành một quy trình ERP end-to-end |

---

## 3. Các module trong repository

| Tên kỹ thuật module | Tên hiển thị trên Odoo | Mục đích chính |
|---|---|---|
| `fruit_fresh_operations` | Fruit Fresh Operations | Mở rộng Lot/Batch, tạo QC Check, ghi nhận Wastage Log, kiểm soát FEFO, gợi ý lô xuất kho và tạo Daily Closing Report |
| `fruit_crm_daily_pricing` | Fruit CRM Daily Pricing | Thu thập thông tin thị trường từ CRM và tạo bảng giá trái cây hằng ngày cho Sales |

---

# 4. Module `fruit_fresh_operations`

## 4.1. Mục đích

`fruit_fresh_operations` mở rộng Odoo Inventory để hỗ trợ nghiệp vụ vận hành trái cây tươi.

Module này tập trung vào các nghiệp vụ:

- Quản lý thông tin mở rộng của Lot/Batch.
- Ghi nhận ngày thu hoạch, hạn sử dụng, phân hạng chất lượng và trạng thái QC.
- Tạo phiếu QC Check trực tiếp từ phiếu nhập kho.
- Xử lý kết quả QC dạng `Passed`, `Failed`, `Partial`.
- Tự động ghi nhận Wastage Log cho phần hàng lỗi/hư.
- Kiểm soát lô hàng theo FEFO.
- Gợi ý lô nên xuất trước khi giao hàng.
- Tổng hợp Daily Fruit Closing Report cho quản lý vận hành.

---

## 4.2. Luồng nghiệp vụ chính

```text
Receipt
→ Create QC Check
→ QC Result: Passed / Failed / Partial
→ Update Lot QC Status
→ Generate Wastage Log for rejected quantity
→ Monitor FEFO Batch Control
→ Use FEFO Suggestion for sales delivery
→ Generate Daily Fruit Closing Report
