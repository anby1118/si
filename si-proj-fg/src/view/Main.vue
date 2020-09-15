<template>
    <div>
        <header class="header">
            <div class="container">
                <div class="header-area">
                    <div class="logo">
                        <a href="index.html"><img src="../assets/img/logo.png" alt="logo" /></a>
                    </div>
                    <div class="header-right">
                        <form action="#">
                            <select>
                                <option value="Movies">Movies</option>
                                <option value="Movies">Movies</option>
                                <option value="Movies">Movies</option>
                            </select>
                            <input type="text" />
                            <button><i class="icofont icofont-search"></i></button>
                        </form>
                        <ul>
                            <li><a href="#">Welcome Guest!</a></li>
                            <li><a class="login-popup" href="#">Login</a></li>
                        </ul>
                    </div>
                    <div class="menu-area">
                        <div class="responsive-menu"></div>
                        <div class="mainmenu">
                            <ul id="primary-menu">
                                <router-link tag="li" to="/home/" exact><a>Home</a></router-link>
                                <router-link tag="li" to="/movies/"><a>Movies</a></router-link>
                                <router-link tag="li" to="/celebrities_list/"><a>CelebritiesList</a></router-link>
                                <router-link tag="li" to="/top_movies/"><a>Top Movies</a></router-link>
                                <router-link tag="li" to="/news/"><a>News</a></router-link>
                                <li><a href="#">Pages <i class="icofont icofont-simple-down"></i></a>
                                    <ul>
                                        <router-link tag="li" to="/blog_details/"><a>Blog Details</a></router-link>
                                        <router-link tag="li" to="/movie_details/"><a>Movie Details</a></router-link>
                                    </ul>
                                </li>
                                <li><a class="theme-btn" href="#"><i class="icofont icofont-ticket"></i> Tickets</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <div class="login-area">
            <div class="login-box">
                <a href="#"><i class="icofont icofont-close"></i></a>
                <h2>LOGIN</h2>
                <Form></Form>
                <form action="#">
                    <h6>USERNAME OR EMAIL ADDRESS</h6>
                    <input type="text" v-model="user.email" />
                    <h6>PASSWORD</h6>
                    <input type="password" v-model="user.pwd" />
                    <div class="login-remember">
                        <input type="checkbox" />
                        <span>Remember Me</span>
                    </div>
                    <div class="login-signup">
                        <span>SIGNUP</span>
                    </div>
                    <a href="#" class="theme-btn" @click="handleSubmit">LOG IN</a>
                    <span>Or Via Social</span>
                    <div class="login-social">
                        <a href="#"><i class="icofont icofont-social-facebook"></i></a>
                        <a href="#"><i class="icofont icofont-social-twitter"></i></a>
                        <a href="#"><i class="icofont icofont-social-linkedin"></i></a>
                        <a href="#"><i class="icofont icofont-social-google-plus"></i></a>
                        <a href="#"><i class="icofont icofont-camera"></i></a>
                    </div>
                </form>

            </div>
        </div>
        <div class="buy-ticket">
            <div class="container">
                <div class="buy-ticket-area">
                    <a href="#"><i class="icofont icofont-close"></i></a>
                    <div class="row">
                        <div class="col-lg-8">
                            <div class="buy-ticket-box">
                                <h4>Buy Tickets</h4>
                                <h5>Seat</h5>
                                <h6>Screen</h6>
                                <div class="ticket-box-table">
                                    <table class="ticket-table-seat">
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                    </table>
                                    <table>
                                        <tr>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>2</td>
                                        </tr>
                                        <tr>
                                            <td>3</td>
                                        </tr>
                                        <tr>
                                            <td>4</td>
                                        </tr>
                                        <tr>
                                            <td>5</td>
                                        </tr>
                                    </table>
                                    <table class="ticket-table-seat">
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td class="active">1</td>
                                            <td class="active">1</td>
                                            <td class="active">1</td>
                                            <td class="active">1</td>
                                            <td class="active">1</td>
                                            <td class="active">1</td>
                                            <td class="active">1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                    </table>
                                    <table>
                                        <tr>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>2</td>
                                        </tr>
                                        <tr>
                                            <td>3</td>
                                        </tr>
                                        <tr>
                                            <td>4</td>
                                        </tr>
                                        <tr>
                                            <td>5</td>
                                        </tr>
                                    </table>
                                    <table class="ticket-table-seat">
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                        <tr>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                            <td>1</td>
                                        </tr>
                                    </table>
                                </div>
                                <div class="ticket-box-available">
                                    <input type="checkbox" />
                                    <span>Available</span>
                                    <input type="checkbox" checked />
                                    <span>Unavailable</span>
                                    <input type="checkbox" />
                                    <span>Selected</span>
                                </div>
                                <a href="#" class="theme-btn">previous</a>
                                <a href="#" class="theme-btn">Next</a>
                            </div>
                        </div>
                        <div class="col-lg-3 offset-lg-1">
                            <div class="buy-ticket-box mtr-30">
                                <h4>Your Information</h4>
                                <ul>
                                    <li>
                                        <p>Location</p>
                                        <span>HB Cinema Box Corner</span>
                                    </li>
                                    <li>
                                        <p>TIME</p>
                                        <span>2018.07.09 20:40</span>
                                    </li>
                                    <li>
                                        <p>Movie name</p>
                                        <span>Home Alone</span>
                                    </li>
                                    <li>
                                        <p>Ticket number</p>
                                        <span>2 Adults, 2 Children, 2 Seniors</span>
                                    </li>
                                    <li>
                                        <p>Price</p>
                                        <span>89$</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- header section end -->
        <router-view></router-view>
        <!-- footer section start -->
        <footer class="footer">
            <div class="container">
                <div class="row">
                    <div class="col-lg-3 col-sm-6">
                        <div class="widget">
                            <img src="../assets/img/logo.png" alt="about" />
                            <p>7th Harley Place, London W1G 8LZ United Kingdom</p>
                            <h6><span>Call us: </span>(+880) 111 222 3456</h6>
                        </div>
                    </div>
                    <div class="col-lg-3 col-sm-6">
                        <div class="widget">
                            <h4>Legal</h4>
                            <ul>
                                <li><a href="#">Terms of Use</a></li>
                                <li><a href="#">Privacy Policy</a></li>
                                <li><a href="#">Security</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-sm-6">
                        <div class="widget">
                            <h4>Account</h4>
                            <ul>
                                <li><a href="#">My Account</a></li>
                                <li><a href="#">Watchlist</a></li>
                                <li><a href="#">Collections</a></li>
                                <li><a href="#">User Guide</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-sm-6">
                        <div class="widget">
                            <h4>Newsletter</h4>
                            <p>Subscribe to our newsletter system now to get latest news from us.</p>
                            <form action="#">
                                <input type="text" placeholder="Enter your email.." />
                                <button>SUBSCRIBE NOW</button>
                            </form>
                        </div>
                    </div>
                </div>
                <hr />
            </div>
            <div class="copyright">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-6 text-center text-lg-left">
                            <div class="copyright-content">
                                <p>&copy; 2018 MoviePoint. All Rights <a href="http://www.sucai8.cn/">Reserved</a>.
                                    Designed by themerocket</p>
                            </div>
                        </div>
                        <div class="col-lg-6 text-center text-lg-right">
                            <div class="copyright-content">
                                <a href="#" class="scrollToTop">
                                    Back to top<i class="icofont icofont-arrow-up"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer><!-- footer section end -->
    </div>
</template>

<script>
    import {
        register,
        // check_token,
        // get_MFtoken
    } from '@/api/user.js'
    import {
        mapActions,
        // mapMutations
    } from 'vuex'
    // import store from '@/store'
    $(document).ready(function() {
        // 严格模式
        "use strict";

        $(window).on('scroll', function() {
            if ($(this).scrollTop() > 600) {
                $('.scrollToTop').fadeIn();
            } else {
                $('.scrollToTop').fadeOut();
            }
        });
        $('.scrollToTop').on('click', function() {
            $('html, body').animate({
                scrollTop: 0
            }, 2000);
            return false;
        });

        $('.menu-area ul > li > .theme-btn').on('click', function() {
            $('.buy-ticket').show();
            return false;
        });
        $('.buy-ticket .buy-ticket-area > a').on('click', function() {
            $('.buy-ticket').hide();
            return false;
        });
        $('.login-popup').on('click', function() {
            $('.login-area').show();
            return false;
        });
        $('.login-box > a').on('click', function() {
            $('.login-area').hide();
            return false;
        });
    });
    export default {
        name: "Main",
        data() {
            return {
                user: {
                    email: '',
                    pwd: '',
                    name: ''
                }
            }
        },
        methods: {
            // 定义随机函数，用于生成浮游用户名和密码
            randomString(len) {
                len = len || 12;
                var $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz012345678_'; /****默认去掉了容易混淆的字符oOLl,9gq,Vv,Uu,I1****/
                var maxPos = $chars.length;
                var pwd = '';
                var i = 0;
                for (i; i < len; i++) {
                    pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
                }
                return pwd;
            },
            // 初始化用户名密码，生成蜉蝣
            initUser() {
                this.user.name = this.randomString(6)
                this.user.email = this.user.name + "@si.mayfly.com";
                this.user.pwd = this.randomString(10)
                return true
            },
            //导入vuex中的action => handleLogin
            ...mapActions([
                'handleLogin'
            ]),
            // ...mapMutations([
            //     'setToken',
            //     'setHMstat'
            // ]),
            handleSubmit() {
                // 调用用户登录action => 调用登录接口，保存数据
                //    |--------------跳转到my页面（后期跳转到需要跳转前的页面）
                const email = this.user.email
                const password = this.user.pwd
                this.handleLogin({
                    email,
                    password
                }).then(
                    res => {
                        console.log("成功!login")
                        console.log(res)
                        // 关闭登录窗口
                        $('.login-area').hide();
                    },
                    reason => {
                        console.log(reason)
                        console.log("失败!login")
                    }).catch(
                    reason => {
                        console.log(reason)
                        console.log("失败!login")
                    })
            },
            // 注册
            registerHandler() {
                register(this.user.name, this.user.email, this.user.pwd).then(
                    // 请求成功的处理方法
                    res => {
                        console.log(res)
                    },
                    // 请求失败的处理方法
                    res => {
                        console.log(res)
                    }
                )
            },
        },
        mounted() {
            // 初始化随机蜉蝣账户
            this.initUser()
            // 验证token,成功获取HMstat,失败就注册，获取MFtoken,登录蜉蝣
            // check_token(store.state.token).then(
            //     res => {
            //         this.setHMstat("True")
            //     },
            //     err => {
            //         console.log(err)
            //         this.setHMstat("False")
            //         // 注册蜉蝣账户
            //         this.registerHandler()
            //         // 向后端发送mayfly请求
            //         // get_MFtoken().then(
            //         //     res => {
            //         //         console.log("成功获取MFtoken")
            //         //         this.setToken(res.data.token)
            //         //         this.setHMstat(res.data.HMstat)
            //         //     },
            //         //     err => {
            //         //         console.log(err)
            //         //         console.log("失败获取MFtoken")
            //         //     }).catch(
            //         //     reason => {
            //         //         console.log(reason)
            //         //     })
                    
            //         this.setToken(err.data.token)
            //         this.setHMstat(err.data.HMstat)
                    
            //         //不需要check_token功能,直接使用token_first向后台取数据，由后端验证token取对应数据
            //         //修改check_token功能，根据权限渲染访问页面，没有权限的页面不显示
            //         //通过父子路由，如果传递值过来就显示，如果没传值过来就不显示
            //         //设置路由守卫，在访问网站的时候就判断token，决定跳转和渲染

            //         // 登录蜉蝣账户
            //         this.handleSubmit()
            //     }
            // ).catch(
            //     reason => {
            //         console.log(reason)
            //     }
            // )

        }
    }
</script>

<style>
</style>
