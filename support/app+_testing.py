from bertopic import BERTopic
import pandas as pd

# Tạo một tập dữ liệu văn bản mô phỏng
documents = [
    "AI đang thay đổi thế giới công nghệ.",
    "Học sâu và máy học là xu hướng hiện tại.",
    "Chứng khoán tăng mạnh sau tin tức kinh tế tốt.",
    "Thời tiết hôm nay rất đẹp và trời trong xanh.",
    "Du lịch hè này rất thú vị với nhiều điểm đến hấp dẫn.",
    "Lập trình Python được sử dụng rộng rãi trong khoa học dữ liệu.",
    "Blockchain và tiền điện tử đang thu hút nhiều nhà đầu tư.",
    "Bóng đá là môn thể thao được yêu thích trên toàn thế giới.",
    "Công nghệ 5G sẽ mở ra kỷ nguyên mới cho Internet vạn vật.",
    "Giá dầu tăng do tình hình chính trị toàn cầu."
]

# Huấn luyện BERTopic
topic_model = BERTopic(language="multilingual")
topics, probs = topic_model.fit_transform(documents)

# Hiển thị chủ đề đã trích xuất
df_topics = pd.DataFrame(topic_model.get_topic_info())
df_topics