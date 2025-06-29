import os
import re


def natural_sort_key(s):
    """
    生成自然排序键，用于实现类似Windows资源管理器的排序
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]


def rename_images_with_names(folder_path, names_file):
    # 读取名字列表
    with open(names_file, 'r', encoding='utf-8') as f:
        names = [line.strip() for line in f if line.strip()]

    # 获取文件夹中所有图片文件
    files = os.listdir(folder_path)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

    # 使用自然排序（不使用natsort库）
    image_files.sort(key=natural_sort_key)

    # 检查名字数量是否足够
    if len(names) < len(image_files):
        print(f"警告: 名字数量({len(names)})少于图片数量({len(image_files)})")
        # 只处理有对应名字的图片
        image_files = image_files[:len(names)]

    # 重命名文件
    for i, (old_name, new_name) in enumerate(zip(image_files, names), 1):
        # 获取文件扩展名
        ext = os.path.splitext(old_name)[1]

        # 构造新文件名（保留原扩展名）
        new_filename = f"{new_name}{ext}"

        # 文件路径
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_filename)

        # 检查是否有重名文件
        if os.path.exists(new_path):
            print(f"{i}. 跳过: {new_filename} 已存在")
            continue

        # 重命名文件
        try:
            os.rename(old_path, new_path)
            print(f"{i}. 重命名: {old_name} → {new_filename}")
        except Exception as e:
            print(f"{i}. 错误: 无法重命名 {old_name} - {str(e)}")


# 使用示例
if __name__ == "__main__":
    # 替换为你的实际路径
    images_folder = input("请输入图片文件夹路径: ").strip('"')
    names_file = input("请输入名字文本文件路径: ").strip('"')

    rename_images_with_names(images_folder, names_file)

    print("\n操作完成！按Enter键退出...")
    input()