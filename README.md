\# Odoo Fruit ERP Custom Addons



Repository này chứa các custom module Odoo được phát triển cho đồ án triển khai ERP trong doanh nghiệp thu mua, phân phối và bán lẻ trái cây tươi. Các module mở rộng luồng nghiệp vụ của Odoo Inventory, CRM, Sales và Pricing nhằm hỗ trợ các nghiệp vụ đặc thù như truy xuất nguồn gốc theo lô, kiểm định chất lượng, ghi nhận hao hụt, kiểm soát tồn kho theo FEFO và tạo bảng giá trái cây hằng ngày dựa trên dữ liệu CRM.



\## Bối cảnh dự án



Dự án mô phỏng việc triển khai Odoo ERP cho một doanh nghiệp kinh doanh trái cây tươi, bao gồm các hoạt động thu mua, phân phối và bán lẻ. Doanh nghiệp gặp một số vấn đề nghiệp vụ đặc thù:



\- Trái cây tươi có vòng đời ngắn, cần được quản lý theo Lot/Batch.

\- Hoạt động xuất kho cần tuân theo nguyên tắc FEFO: First Expired, First Out.

\- Hàng nhập từ nhà cung cấp cần được kiểm định chất lượng trước khi đưa vào kho bán.

\- Hàng hư, dập, lỗi hoặc không đạt chuẩn cần được ghi nhận thành hao hụt/wastage.

\- Giá bán trái cây có thể thay đổi hằng ngày dựa trên tín hiệu thị trường, nhu cầu CRM, giá đối thủ và giá mua đầu vào.

\- Các nghiệp vụ Sales, Purchase, Inventory, CRM và Accounting/report cần được kết nối thành một quy trình ERP end-to-end.



\## Các module trong repository



| Tên kỹ thuật module | Tên hiển thị trên Odoo | Mục đích chính |

|---|---|---|

| `fruit\_fresh\_operations` | Fruit Fresh Operations | Mở rộng Lot/Batch, tạo QC Check, ghi nhận Wastage Log, kiểm soát FEFO, gợi ý lô xuất kho và tạo Daily Closing Report |

| `fruit\_crm\_daily\_pricing` | Fruit CRM Daily Pricing | Thu thập thông tin thị trường từ CRM và tạo bảng giá trái cây hằng ngày cho Sales |



\---



\# 1. fruit\_fresh\_operations



\## Mục đích



`fruit\_fresh\_operations` mở rộng Odoo Inventory để hỗ trợ các nghiệp vụ đặc thù của ngành trái cây tươi. Module tập trung vào:



\- Mở rộng thông tin Lot/Batch.

\- Kiểm định chất lượng hàng nhập kho.

\- Xử lý kết quả QC dạng Passed / Failed / Partial.

\- Ghi nhận hao hụt đối với hàng hư, dập, lỗi hoặc không đạt chuẩn.

\- Kiểm soát Lot/Batch theo nguyên tắc FEFO.

\- Gợi ý lô hàng nên xuất trước khi giao hàng.

\- Tạo báo cáo đóng ngày cho vận hành trái cây.



\## Luồng nghiệp vụ chính



```text

Receipt

→ Create QC Check

→ QC Result: Passed / Failed / Partial

→ Update Lot QC Status

→ Generate Wastage Log for rejected quantity

→ Monitor FEFO Batch Control

→ Use FEFO Suggestion for sales delivery

→ Generate Daily Fruit Closing Report

