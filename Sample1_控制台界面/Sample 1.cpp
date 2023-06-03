#include<bits/stdc++.h>
#include<fstream>
#include<conio.h>
using namespace std;
const int &INF=114514;
void welcome();
void work();
void error();
void input1();
void input2();
int check(string s);
void floyd();
map<int,string>place;
int graph[114][114],path[514][514];
int place_a=0,place_b=0,n=16;
int main()
{
	welcome();
	string command;
	while(1) {
		getline(cin,command);
		if(command.size()>1)error();
		else if(command.size()==0) {
			for(int i=1; i<=n; i++) {
				for(int j=1; j<=n; j++) {
					graph[i][j]=INF;
					path[i][j]=j;
				}
			}
			work();
			cout<<endl<<"输入回车以开始新一轮导航"<<endl;
		} else if(command.size()==1&&command[0]=='N') {
			cout<<"欢迎下次使用"<<endl;
			system("pause");
			exit(0);
		} else error();
	}
	system("pause>nul");
	return 0;
}
void welcome()
{
	cout<<"========================欢迎使用广东外语外贸大学校园导航=======================\n"
	    "=====                   Welcome to the GDUFS Navigation                   =====\n"
	    "====                                                                       ====\n"
	    "===        1.三饭         2.南苑           3.中行快递点     4.又康          ===\n"
	    "==                                                                           ==\n"
	    "==         5.北苑         6.二饭（已倒闭） 7.下沉广场       8.一饭           ==\n"
	    "==                                                                           ==\n"
	    "==         9.水电充值点   10.后勤处        11.门诊部        12.教学楼群      ==\n"
	    "==                                                                           ==\n"
	    "==         13.图书馆      14.实验楼群      15.艺术学院      16.体育馆        ==\n"
	    "==                                                                           ==\n"
	    "===                                                                         ===\n"
	    "====                 输入回车开始导航       输入N退出系统                  ====\n"
	    "=====                                                                     =====\n"
	    "===============================================================================\n";
}
void work()
{
	input1();
	input2();
	string x,y;
	while(1) {
		cout<<"请输入起点"<<endl;
		getline(cin,x);
		if(x=="N") {
			cout<<"欢迎下次使用"<<endl;
			system("pause");
			exit(0);
		} else if(!check(x)||x.size()==0)error();
		else {
			place_a=stoi(x);
			if(place_a>=1&&place_a<=16)break;
			else error();
		}
	}
	bool flag=0;
	while(1) {
		cout<<"请输入终点"<<endl;
		getline(cin,y);
		if(y=="N") {
			cout<<"欢迎下次使用"<<endl;
			system("pause");
			exit(0);
		} else if(!check(y)||y.size()==0)error();
		else {
			place_b=stoi(y);
			if(place_b>=1&&place_b<=16&&place_b!=place_a)break;
			else if(place_a==place_b) {
				cout<<"您是否误输数据了呢？"<<endl;
				cout<<"原地 -> 原地 的最短路径长度是: 0米 呀~"<<endl;
				flag=1;
				break;
			} else error();
		}
	}
	if(!flag) {
		cout<<"-----------------------------------------------------"<<endl;
		cout<<endl<<"| "<<place[place_a]<<" -> "<<place[place_b]<<" 的最短路径长度是："<<graph[place_a][place_b]<<"米 |"<<endl<<endl;
		cout<<"-----------------------------------------------------"<<endl;
		int path_detail[114]= {0},cnt=0;
		cout<<"具体路径是："<<endl;
		while (place_a!=place_b) {
			cnt++;
			path_detail[cnt]=place_a;
			place_a=path[place_a][place_b];
		}
		path_detail[++cnt]=place_b;
		for(int i=1; i<cnt; i++) {
			cout<<place[path_detail[i]]<<" -> "<<place[path_detail[i+1]]<<": "<<graph[path_detail[i]][path_detail[i+1]]<<" 米\t"<<endl;
		}
		cout<<endl<<"本次导航结束"<<endl;
	}
}
void input1()
{
	ifstream ifs;
	ifs.open("placedata.txt",ios::in);
	if(!ifs.is_open()) {
		cout<<"很抱歉，程序所需文件placedata.txt丢失"<<endl;
		system("pause");
		exit(0);
	} else {
		string placedata;
		while(getline(ifs,placedata)) {
			if(isdigit(placedata[0])) {
				int placeid=stoi(placedata.substr(0,placedata.find(' ')));
				placedata.erase(0,placedata.find(' ')+1);
				string placename=placedata.substr(0,placedata.size());
				place[placeid]=placename;
			}
		}
	}
}
void input2()
{
	ifstream ifs;
	ifs.open("routedata.txt",ios::in);
	if(!ifs.is_open()) {
		cout<<"很抱歉，程序所需文件routedata.txt丢失"<<endl;
		system("pause");
		exit(0);
	} else {
		string routedata;
		while(getline(ifs,routedata)) {
			if(isdigit(routedata[0])) {
				int a=stoi(routedata.substr(0,routedata.find(' ')));
				routedata.erase(0,routedata.find(' ')+1);
				int b=stoi(routedata.substr(0,routedata.find(' ')));
				routedata.erase(0,routedata.find(' ')+1);
				int distance=stoi(routedata.substr(0,routedata.size()));
				graph[a][b]=distance;
				graph[b][a]=distance;
			}
		}
		floyd();
	}
}
int check(string s)
{
	if(s.size()>2)return 0;
	for(int i=0; i<s.size(); i++) {
		if(!isdigit(s[i]))return 0;
	}
	return 1;
}
void error()
{
	cout<<"指令或数据错误，请重试"<<endl<<endl;
}
void floyd()
{
	for(int k=1; k<=n; k++) {
		for(int i=1; i<=n; i++) {
			for(int j=1; j<=n; j++) {
				if(graph[i][j]>graph[i][k]+graph[k][j]) {
					graph[i][j]=graph[i][k]+graph[k][j];
					path[i][j]=path[i][k];
				}
			}
		}
	}
}
