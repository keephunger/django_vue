<template>
    <section class="todoapp">
        <header class="header">
            <h1>todos</h1>
            <input class="new-todo" placeholder="What needs to be done?" autofocus
                   @keydown.enter="add_list($event.target)" ref="currentInput">
        </header>
        <!-- This section should be hidden by default and shown when there are todos -->
        <section class="main">
            <input id="toggle-all" class="toggle-all" type="checkbox" v-model='flag1'>
            <label @click="show_all(flag1)" for="toggle-all">Mark all as complete</label>
            <ul class="todo-list">
                <!-- These are here just to show the structure of the list items -->
                <!-- List items should get the class `editing` when editing and `completed` when marked as completed -->
                <li v-if="value.show" v-bind:class=" value.status ? 'completed' : '' " v-for="(value,index) in list"
                    :key="index">
                    <div class="view" v-if="!value.edit">
                        <input class="toggle" type="checkbox" v-model="value.status" @change="completed_list(value)">
                        <label @dblclick="edit_list(value)">{{value.text}}</label>
                        <button class="destroy" @click="remove_list(index)"></button>
                    </div>
                    <input v-bind:class="value.edit ?'editing':'edit'" v-model="value.text"
                           @blur="change_list($event.target,value)">
                </li>
            </ul>
        </section>
        <!-- This footer should hidden by default and shown when there are todos -->
        <footer class="footer">
            <!-- This should be `0 items left` by default -->
            <span class="todo-count"><strong>{{list.length}}</strong> item left</span>
            <!-- Remove this if you don't implement routing -->
            <ul class="filters">
                <li>
                    <a class="selected" href="#/" @click="show_all(1)">All</a>
                </li>
                <li>
                    <a href="#/active" @click="show_active()">Active</a>
                </li>
                <li>
                    <a href="#/completed" @click="show_completed()">Completed</a>
                </li>
            </ul>
            <!-- Hidden if no completed items are left ↓ -->
            <button class="clear-completed" @click="clear_completed()">Clear completed</button>
        </footer>
    </section>

</template>
<script>
    import {mapState, mapActions} from 'vuex'

    export default {
        data() {
            return {
                flag1: true
            }
        },
        methods: {
            ...mapActions('messages', [
                'addMessage',
                'deleteMessage',
            ]),
            remove_list: function (index) {
                this.$options.methods.deleteMessage.bind(this)(this.list[index].pk)
            },
            add_list: function (e) {
                var val = e.value
                if (val === "") {
                    return
                } //如果输入内容为空则立即返回
                // this.list = this.list.concat({
                //     text: val,
                //     status: false,
                //     edit: false,
                //     show: true
                // })
                this.$options.methods.addMessage.bind(this)({
                    text: val,
                    status: false,
                    edit: false,
                    show: true
                })
                this.$refs.currentInput.value = "" //按下enter添加todo之后把输入框value清零
            },
            edit_list: function (value) {
                value.edit = true
            },
            change_list: function (e, value) {
                value.text = e.value
                value.edit = false
                this.$options.methods.deleteMessage.bind(this)(value.pk)
                this.$options.methods.addMessage.bind(this)(value)
            },
            show_all: function (flag) {

                flag ? this.list.map(list => list.show = true) : this.list.map(list => list.show = false)
            },
            show_active: function () {
                this.list.map(list => list.status ? list.show = false : list.show = true)
            },
            show_completed: function () {
                this.list.map(list => list.status ? list.show = true : list.show = false)
            },
            clear_completed: function () {
                for (let i = 0; i < this.list.length; i++) {
                    if (this.list[i].status) {
                        this.$options.methods.deleteMessage.bind(this)(this.list[i].pk)
                        i--//length 会改变所以i--
                    }
                }
            },
            completed_list: function (value) {
                this.$options.methods.deleteMessage.bind(this)(value.pk)
                this.$options.methods.addMessage.bind(this)(value)
            }
        },
        computed: mapState({
            list: state => state.messages.messages
        }),
        created() {
            this.$store.dispatch('messages/getMessages')
        },
    }

</script>