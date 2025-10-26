import random
import string

def generate_random_word(min_length=3, max_length=12):
    """生成一個隨機長度的字串"""
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_word_list(count=100000, output_file='random_words.txt'):
    """生成指定數量的隨機字串並寫入文件"""
    print(f"開始生成 {count:,} 個隨機字串...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(count):
            word = generate_random_word()
            f.write(word + '\n')
            
            # 每 10000 個字顯示進度
            if (i + 1) % 10000 == 0:
                print(f"已生成: {i + 1:,} 個字串")
    
    print(f"\n完成! 已生成 {count:,} 個隨機字串到 '{output_file}'")

# 執行程式
if __name__ == "__main__":
    generate_word_list(count=100000, output_file='random_words.txt')