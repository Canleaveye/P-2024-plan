// 利用排序算法解决实际问题
// 冒泡(选择)排序
// 实际问题：高中分班考试成绩出来了，现电脑老师有所有同学的综合成绩，要将同学们按照成绩由高到低的顺序排序，并进行分班,每班10人，共10个班,并给他们分配好各自的学号
#include<stdio.h>
#include<stdlib.h>
#define Max_num 100
struct stu
{
    int num;
    int score;
};

// 生成学号
void Prdnum(struct stu stui[], int length)
{
    for (int i = 1; i <= length; i++)
    {
        stui[i].num = 2024*100 + i;
    }
}
// 随机生成学生成绩的函数(不知道怎么设置才能使生成的成绩正态分布)
void Produce(struct stu stui[], int length)
{
    for (int i = 1; i <= length; i++)
    {

        stui[i].score = 40 + rand() % 61;
    }
}
// 将学生成绩进行排名
void Sort(struct stu stui[], int length)
{
    for (int i = 0; i < length; i++)
    {
        int k = i;
        for (int j = i + 1; j < length; j++)
        {
            if (stui[j].score < stui[k].score)
                k = j;
        }
        int temp1 = stui[i].score;
        stui[i].score = stui[k].score;
        stui[k].score = temp1;
        int temp2 = stui[i].num;
        stui[i].num = stui[k].num;
        stui[k].num = temp2;
    }
}
void Print(struct stu stui[], int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("stu%d %d     ",stui[i].num , stui[i].score);
    }
    printf("\n-----------\n");
}
// 分班函数
void Class(struct stu stui[] ,int length)
{

    for (int n = 1; n <= 10; n++)
    {
        printf("class%d: ", n);
        for (int i = 0; i < 10; i++)
        {
            printf("%d ", stui[(n - 1) * 10 + i].num);
        }
    }
}
// 定义结构体包括学生学号和成绩

int main()
{
    // 1：设置学生总人数
    struct stu stui[Max_num];
    // 2.生成学生学号
    Prdnum(stui, Max_num);
    //3.随机生成同学们的成绩并将成绩存入数组中
    srand((unsigned int)time(NULL));
    Produce(stui, Max_num);
    // 4.将成绩排序
    Sort(stui, Max_num);
    // 5.输出排序后的学生成绩
    Print(stui, Max_num);
        // 第五步，将成绩按照一定的规则分班，输出同学们的学号和班级号
    Class(stui, Max_num);
    system("pause");
    return 0;
}

