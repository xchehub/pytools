import random

# pip install nltk

def load_dictionary():
    """載入系統字典或使用內建單字列表"""
    try:
        # 嘗試從系統字典載入（Linux/Mac）
        with open('/usr/share/dict/words', 'r', encoding='utf-8') as f:
            words = [word.strip().lower() for word in f if word.strip().isalpha()]
        print(f"從系統字典載入了 {len(words):,} 個單字")
        return words
    except FileNotFoundError:
        print("系統字典未找到，請使用 nltk 或提供單字文件")
        return None

def load_dictionary_nltk():
    """使用 NLTK 載入英文單字"""
    try:
        import nltk
        nltk.download('words', quiet=True)
        from nltk.corpus import words
        word_list = [word.lower() for word in words.words()]
        print(f"從 NLTK 載入了 {len(word_list):,} 個單字")
        return word_list
    except ImportError:
        print("NLTK 未安裝，請執行: pip install nltk")
        return None

def generate_word_list(count=100000, output_file='random_words.txt'):
    """從字典中隨機選擇單字並寫入文件"""
    
    # 優先嘗試系統字典，再嘗試 NLTK
    dictionary = load_dictionary()
    if dictionary is None:
        dictionary = load_dictionary_nltk()
    
    if dictionary is None or len(dictionary) == 0:
        print("錯誤：無法載入字典！")
        return
    
    print(f"\n開始生成 {count:,} 個隨機單字...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(count):
            # 從字典中隨機選擇一個單字（可重複）
            word = random.choice(dictionary)
            f.write(word + '\n')
            
            # 每 10000 個字顯示進度
            if (i + 1) % 10000 == 0:
                print(f"已生成: {i + 1:,} 個單字")
    
    print(f"\n完成! 已生成 {count:,} 個隨機單字到 '{output_file}'")

# 執行程式
if __name__ == "__main__":
    generate_word_list(count=100000, output_file='random_words.txt')