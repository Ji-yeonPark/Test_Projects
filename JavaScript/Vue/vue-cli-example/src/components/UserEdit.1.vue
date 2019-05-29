<template>
  <div class="yellow lighten-3 pa-3">
    <h3>회원 정보를 수정할 수 있습니다.</h3>
    <p>수정사항</p>
    <v-text-field label="Regular" v-model="user.name"></v-text-field>
    // 값을 변경해도 자식 컴포넌트 내의 user객체 값이 변경되는 것이기 때문에 에러 발생 X
  </div>
</template>

<script>
export default {
  props: ["name", "address", "phone", "hasDog"],
  data() {
    return {
      user: {}
    };
  },
  created() {
    this.user.name = this.name;
    this.user.address = this.address;
    this.user.phone = this.phone;
    this.user.hasDog = this.hasDog;
  }
};
</script>
