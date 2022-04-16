

##  NPM

###  介绍

1. 全称：Node Package Manager, Node的包管理器，也是一个应用程序
2. Node.js 的包基本遵循 CommonJS 规范，将一组相关的模块组合在一起，形成一个完整的工具
3. 通过 NPM 可以对 Node 的工具包进行搜索、下载、安装、删除、上传。借助别人写好的包，可以让我们的开发更加方便。
4. 安装完 nodejs 之后会自动安装 npm

### 常用命令

1. 查看版本

   ```sh
   npm -v 
   ```

2. 初始化

   ```sh
   npm init
   npm init --yes
   ```

3. package.json文件

   ```json
   {
     "name":  "1-npm",     #包的名字
     "version": "1.0.0",   #包的版本
     "description": "",    #包的描述
     "main": "index.js",   #包的入口文件
     "scripts": {			#脚本配置
       "test": "echo \"Error: no test     specified\" && exit 1" 
      },
     "author": "",			#作者
     "license": "ISC"		#版权声明
   }
   ```

4. 包名不能使用中文，大写和 npm 作为包的名字

5. 搜索包

   ```sh
   npm search jquery
   npm s jquery
   ```

6. 安装包

   ```sh
   npm install name
   npm i name
   # 安装并在 package.json 中保存包的信息(dependencies 属性)(版本6默认保存)
   npm install jquery --save
   npm install jquery -S
   # 安装并在 package.json 中保存包的信息(devDependencies 属性)
   npm install babel --save-dev
   npm install babel -D
   ```

7. 全局安装

   ```sh
   npm i name -g
   ```

   ```
   // 安装的位置 
   // 全局安装命令在任意的命令行下, 都可以执行
   C:\Users\你的用户名\AppData\Roaming\npm
   ```

8. 安装依赖

   ```sh
   npm i
   npm i --production // 只安装 dependencies 中的依赖
   ```

9. 删除包

   ```sh
   npm remove jquery
   ```

### 使用流程

1. 从仓库中拉取仓库代码
2. 运行 npm i 安装相关依赖
3. 运行项目，继续开发

###  Yarn

#### 介绍

* yarn 是 Facebook 开源的新的包管理器，可以用来代替 npm。

#### 特点

* 本地缓存。安装过的包下次不会进行远程安装
* 并行下载。一次下载多个包，而 npm 是串行下载
* 精准的版本控制。保证每次安装跟上次都是一样的

#### 安装

```sh
npm install yarn -g
```

#### 常用命令

```sh
yarn --version
yarn init 
```

```sh
yarn global add package-name //全局安装
```

``C:\Users\你的用户名\AppData\Local\Yarn\bin``

```sh
yarn global remove name  // 移除全局包
yarn add name         // 局部安装包
yarn add name --dev   // 相当于npm中的--save-dev
yarn remove name      // 局部移除包
yarn list             // 列出所有安装的包
yarn                  //安装package.json中的所有依赖 
//  修改仓库地址
yarn config set registry https://registry.npm.taobao.org
```

### CYarn

* 

### CNpm

* 



### 版本号

#### 版本格式

* "^3.0.0" : 包是3.x.x版本，x默认取最新的。
* "~3.1.x" : 包是3.1.x版本，x默认取最新的
* "3.1.1"   : 包必须是3.1.1版本。

#### 安装指定版本工具包

```
yarn add jquery@1.11.2
```

### npm 清除缓存

```
npm cache clean
```

