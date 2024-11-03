#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import scrolledtext, Menu, messagebox
import math

# 右键复制
def copy_text(event, text_widget):
	try:
		# 获取选中的文本
		selected_text = text_widget.get("sel.first", "sel.last")
		if selected_text:
			text_widget.clipboard_clear()
			text_widget.clipboard_append(selected_text)
	except tk.TclError:
		pass  # 如果没有选中文本，忽略错误

# 右键粘贴
def paste_text(event, text_widget):
	try:
		text_widget.insert(tk.INSERT, text_widget.clipboard_get())
	except tk.TclError:
		pass  # 如果剪贴板为空，忽略错误

# 右键剪切
def cut_text(event, text_widget):
	try:
		selected_text = text_widget.get("sel.first", "sel.last")
		if selected_text:
			text_widget.clipboard_clear()
			text_widget.clipboard_append(selected_text)
			text_widget.delete("sel.first", "sel.last")
	except tk.TclError:
		pass

# 右键菜单
def show_context_menu(event, text_widget):
	# 创建上下文菜单
	context_menu = Menu(text_widget, tearoff=0)
	context_menu.add_command(label="复制", command=lambda e=event: copy_text(e, text_widget))
	context_menu.add_command(label="粘贴", command=lambda e=event: paste_text(e, text_widget))
	context_menu.add_command(label="剪切", command=lambda e=event: cut_text(e, text_widget))
	# 在鼠标右键点击的位置显示菜单
	context_menu.tk_popup(event.x_root, event.y_root)
	context_menu.grab_release()

# 清空输入输出框
def clear_text(*text_widgets):
	for text_widget in text_widgets:
		if text_widget.cget('state') == tk.DISABLED:
			text_widget.config(state=tk.NORMAL)
			text_widget.delete("1.0", tk.END)
			text_widget.config(state=tk.DISABLED)
		else:
			text_widget.delete("1.0", tk.END)

# 编辑文本框
def edit_text(text_widget, data):
	if text_widget.cget('state') == tk.DISABLED:
		text_widget.config(state=tk.NORMAL)
		text_widget.delete("1.0", tk.END)
		text_widget.insert(tk.END, data)
		text_widget.config(state=tk.DISABLED)
	else:
		text_widget.delete("1.0", tk.END)
		text_widget.insert(tk.END, data)

# 获取伤害上限
def get_maximum_damage_limit():
	maximum_damage_limit_str = maximum_damage_limit_text.get("1.0", tk.END)
	maximum_damage_limit_str = maximum_damage_limit_str.strip()
	if maximum_damage_limit_str == "":
		return 300000
		
	try:
		maximum_damage_limit = int(maximum_damage_limit_str, 0)
	except Exception as e:
		edit_text(output_text, f"[-] {e}")
		return -1

	return maximum_damage_limit


def get_input():
	input_text_str = input_text.get("1.0", tk.END)
	input_text_str = input_text_str.strip()
	if input_text_str == "":
		clear_text(output_text)
		return 0

	try:
		input_val = int(input_text_str, 0)
	except Exception as e:
		edit_text(output_text, f"[-] {e}")
		return -1

	return input_val


# 伤害奖励转换伤害值
def damage_value():
	maximum_damage_limit = get_maximum_damage_limit()
	if (maximum_damage_limit == -1):
		return

	damage_reward = get_input()
	if (damage_reward == -1):
		return

	damage_value = math.e ** (damage_reward / maximum_damage_limit - 1 + math.log(maximum_damage_limit*100))
	edit_text(output_text, int(damage_value))

# 伤害值转换伤害奖励
def damage_reward():
	maximum_damage_limit = get_maximum_damage_limit()
	if (maximum_damage_limit == -1):
		return

	damage_value = get_input()
	if (damage_value == -1):
		return

	damage_reward = 0
	if (damage_value <= maximum_damage_limit*100):
		damage_reward = damage_value / 100
	else:
		damage_reward = maximum_damage_limit*(1+math.log(damage_value)-math.log(maximum_damage_limit*100))
	edit_text(output_text, int(damage_reward))

root = tk.Tk()
root.title("伤害分计算")

# 配置主窗口的列和行的伸展
root.grid_columnconfigure(0, weight=1)  # 第0列会随着窗口调整大小
root.grid_columnconfigure(1, weight=1)  # 第1列会随着窗口调整大小

root.grid_rowconfigure(0, weight=1)     # input_frame随着窗口调整大小
root.grid_rowconfigure(1, weight=1)     # output_frame会随着窗口调整大小

# 创建一个新的 Frame 用于输入文本框
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
# 配置输入框架的列和行的伸展框架的列和行的伸展
input_frame.grid_columnconfigure(0, weight=1)  # 使输出框占满整列
input_frame.grid_columnconfigure(1, weight=1)  # 使输出框占满整列
input_frame.grid_rowconfigure(1, weight=1)     # 使input_text输入框占满整行
input_frame.grid_rowconfigure(3, weight=1)     # 使maximum_damage_limit_text输入框占满整行

# 输入标签
input_label = tk.Label(input_frame, text="输入伤害奖励 / 伤害值")
input_label.grid(row=0, column=0, padx=5, pady=0, sticky="w")
# 输入框
input_text = scrolledtext.ScrolledText(input_frame, 
	wrap=tk.WORD, width=50, height=3)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=0, sticky="nsew")
# 绑定鼠标右键点击事件到上下文菜单
input_text.bind("<Button-3>", lambda event, tw=input_text: show_context_menu(event, tw))

# 输入标签
maximum_damage_limit_label = tk.Label(input_frame, text="伤害上限（默认为300000）")
maximum_damage_limit_label.grid(row=2, column=0, padx=5, pady=0, sticky="w")
# 输入框
maximum_damage_limit_text = scrolledtext.ScrolledText(input_frame, 
	wrap=tk.WORD, width=50, height=3)
maximum_damage_limit_text.grid(row=3, column=0, columnspan=2, padx=10, pady=0, sticky="nsew")
# 绑定鼠标右键点击事件到上下文菜单
maximum_damage_limit_text.bind("<Button-3>", 
	lambda event, tw=maximum_damage_limit_text: show_context_menu(event, tw))

#按钮
damage_value_button = tk.Button(input_frame, 
	width=20, text="伤害奖励->伤害值", command=damage_value)
damage_value_button.grid(row=4, column=0, padx=0, pady=(10,0))
#按钮
damage_reward_button = tk.Button(input_frame, 
	width=20, text="伤害值->伤害奖励", command=damage_reward)
damage_reward_button.grid(row=4, column=1, padx=0, pady=(10,0))


# 创建一个新的 Frame 用于输出文本框
output_frame = tk.Frame(root)
output_frame.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")
# 配置输出框架的列和行的伸展
output_frame.grid_columnconfigure(0, weight=1)  # 使输出框占满整列
output_frame.grid_rowconfigure(1, weight=1)     # 使第一个输出框占满整行

# 输出标签
output_label2 = tk.Label(output_frame, text="输出")
output_label2.grid(row=0, column=0, padx=5, pady=0, sticky="w")

# 输出框
output_text = scrolledtext.ScrolledText(output_frame, 
	wrap=tk.WORD, width=50, height=3, state=tk.DISABLED)
output_text.grid(row=1, column=0, padx=10, pady=0, sticky="nsew")
# 绑定鼠标右键点击事件到上下文菜单
output_text.bind("<Button-3>", lambda event, tw=output_text: show_context_menu(event, tw))

# 创建清空按钮
clear_button = tk.Button(root, 
	width=20, text="清空", 
	command=lambda: clear_text(input_text, maximum_damage_limit_text, output_text))
clear_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
