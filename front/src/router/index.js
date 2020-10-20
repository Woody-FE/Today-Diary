import Vue from 'vue';
import VueRouter from 'vue-router';
Vue.use(VueRouter);

const routes = [
	{
		path: '/test',
		name: 'test',
		component: () => import('@/views/Test.vue'),
	},
	{
		path: '/diary',
		name: 'diary',
		component: () => import('@/views/WriteDiaryPage.vue'),
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
