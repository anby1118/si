import Vue from 'vue';
import Router from 'vue-router';

import Main from '../view/Main.vue';

Vue.use(Router);

export default new Router({
    routes: [{
        path: "/",
        name: "main",
        component: Main,
        redirect: "/home/",
        children: [{
                path: "/home/",
                name: "home",
                meta: {title: '首页'},
                title: "首页",
                component: () => import("view/Home.vue")
            },
            {
                path: "/movies/",
                name: "movies",
                component: () => import("view/Movies.vue")
            },
            {
                path: "/celebrities_list/",
                name: "celebrities_list",
                component: () => import("view/CelebritiesList.vue")
            },
            {
                path: "/top_movies/",
                name: "top_movies",
                component: () => import("view/TopMovies.vue")
            },
            {
                path: "/news/",
                name: "news",
                component: () => import("view/News.vue")
            },
            {
                path: "/blog_details/",
                name: "blog_details",
                component: () => import("view/BlogDetails.vue")
            },
            {
                path: "/movie_details/",
                name: "movie_details",
                component: () => import("view/MovieDetails.vue")
            },
        ]
    }]
});
