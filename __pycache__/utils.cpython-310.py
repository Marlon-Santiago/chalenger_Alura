o
    ��d�  �                   @   s�   d dl Zd dlZd dlmZ d dlZd dl	m
Z
mZmZmZmZ ddededefdd	�Zddefdd�Z				ddd�Zdd� ZdS )�    N)�confusion_matrix�accuracy_score�precision_score�recall_score�f1_score��   �   F�label_x�figsize�smallc           
      C   s�   t j|d� ddddd�}tjd|d� tj||| dd�}|�� �d� t j|dd	d
� t j|dd� t j	dd� |j
D ]}	|rH|j|	dd� q<|j|	dddd� q<t ��  d S )N�r   F)zaxes.spines.rightzaxes.spines.topzaxes.spines.leftzaxes.spines.bottom�ticks)�style�rc�viridis)�x�hue�data�palette�   �left)�fontsize�loc�   �r   �   i�����white)r   �padding�color)�plt�figure�sns�	set_theme�	countplot�	get_yaxis�set_visible�title�xlabel�xticks�
containers�	bar_label�show)
Zdadosr   Ztitulor
   r   r   r   Zcustom_params�ax�	container� r/   �?c:\Users\Marlon\Documents\MeusProjetos\chalenger_Alura\utils.py�plot_countplot   s   �
r1   �r   �   c                 C   s4   | � � }tj|d� tj||jj|jjddd� d S )Nr   Tr   )�xticklabels�yticklabels�annot�cmap)�corrr    r!   r"   �heatmap�columns�values)�dfr   r8   r/   r/   r0   �heatmap_corr   s   
�r=   �autoTr   c              	   C   s^  t | |�}dd� t|j�D �}|r t|�|jkr dd� |D �}n|}|r.dd� |�� D �}n|}dd� t||�D �}t�|��|j	d |j	d �}|rht
| |�}t| |�}t| |�}t| |�}d�||||�}nd	}|d krttj�d
�}|dkrzd}tj|d� tjdd� tj||d	|	|||d� tjddd� tjd| dd� |
r�tj|
dd� d S d S )Nc                 S   s   g | ]}d �qS )� r/   )�.0�ir/   r/   r0   �
<listcomp>0   s    z(plot_matriz_confusao.<locals>.<listcomp>c                 S   �   g | ]}d � |��qS )z{}
��format�r@   �valuer/   r/   r0   rB   3   �    c                 S   rC   )z	{0:0.0f}
rD   rF   r/   r/   r0   rB   8   rH   c                 S   s    g | ]\}}|� |� �� � �qS r/   )�strip)r@   �v1�v2r/   r/   r0   rB   <   s    �r   �   uE   

Acurácia={:0.3f}
Precisão={:0.3f}
Recall={:0.3f}
F1 Score={:0.3f}r?   zfigure.figsizeFr   gffffff�?)�
font_scale)r6   �fmtr7   �cbarr4   r5   zValores verdadeiros�   r   zValores preditos�   )r   �range�size�len�flatten�zip�np�asarray�reshape�shaper   r   r   r   rE   r    �rcParams�getr!   r"   �setr9   �ylabelr(   r'   )�y_true_teste�y_pred_teste�group_names�
categories�countrO   ZxyticksZ	sum_statsr   r7   r'   �cfZblanksZgroup_labelsZgroup_countsZ
box_labels�accuracy�	precision�recallZf1_score_metricZ
stats_textr/   r/   r0   �plot_matriz_confusao)   sF   
�



���rh   c              	   C   s�   g }g }g }g }	|D ]"}
|� t||
�� |� t||
�� |� t||
�� |	� t||
�� q
g }|D ]
}|� t||�� q1t�||||||	d��}|j| dd�jdd�S )u�   

    metrica: {'Acurácia Treino', 'Acurácia Teste', 'Precisão', 'Recall', 'F1-Score'}

    Returns:
        DataFrame ordenado de acordo com a métrica passada. 
    )ZModelou   Acurácia Treinou   Acurácia Testeu	   PrecisãoZRecallzF1-ScoreF)�by�	ascendingT)�drop)	�appendr   r   r   r   �pd�	DataFrame�sort_values�reset_index)ZmetricaZnomes_modelosZy_true_treinoZy_pred_treinosr_   Zy_pred_testes�accrf   rg   �f1r`   Z
acc_treinoZy_pred_treinoZtabelar/   r/   r0   �compara_modelos_metricas]   s    	�rs   )r   NF)r2   )	Nr>   TTTTNr   N)�pandasrm   �seabornr"   �matplotlib.pyplot�pyplotr    �numpyrW   Zsklearn.metricsr   r   r   r   r   �str�tuple�boolr1   r=   rh   rs   r/   r/   r/   r0   �<module>   s    

�4