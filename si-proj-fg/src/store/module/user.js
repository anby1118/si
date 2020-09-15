import {
    login,
    // check_token
} from '@/api/user'
import {
    setToken,
    getToken
} from '@/libs/util'

export default {
    state: {
        // 共享的数据
        token: getToken(),
        HMstat: ''
    },
    getters: {},
    mutations: {
        //
        // setToken自定义名字,state参数1,token参数2是用户传递过来的
        setToken(state, token) {
            state.token = token
            setToken(token)
        },
        setHMstat(state, HMstat) {
            state.HMstat = HMstat
        }
    },
    actions: {
        handleLogin(context, value) {
            const email = value.email
            const password = value.password

            // 直接调用login-api.
            // 为了让vue组件中能正确地捕获到当前执行的状态,此处我们返回一个Promise
            // https://www.jianshu.com/p/1b63a13c2701
            return new Promise((resolve, reject) => {
                login(email, password).then(res => {
                    console.log("success")
                    // 保存token
                    context.commit("setToken", res.data.token)
                    resolve()
                }).catch(err => {
                    console.log("fail")
                    reject(err)
                })
            })
        },
        // handleToken(context, value){
        //     const token = value.token
        //     const HMstat = value.HMstat
            
        //     return new Promise((resolve, reject) => {
        //         check_token(token).then(res => {
        //             console.log("check, success")
        //             // 保存token，HMstat
        //             context.commit("setToken", res.data.token)
        //             context.commit("setHMstat", res.data.HMstat)
        //             resolve()
        //         }).catch(err => {
        //             console.log("check, fail")
        //             reject(err)
        //         })
        //     })
        // }
    },
    modules: {
        // 
    }
}
