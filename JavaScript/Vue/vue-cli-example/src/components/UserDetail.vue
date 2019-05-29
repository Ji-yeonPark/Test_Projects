<template>
  <div class="red lighten-3 pa-3">
    <h3>자세한 회원 정보를 확인합니다.</h3>
    <p>상세사항</p>
    <v-list dense>
      <v-list-tile>
        <v-list-tile-content>이름 :</v-list-tile-content>
        <v-list-tile-content class="align-end">{{ name }}</v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>주소 :</v-list-tile-content>
        <v-list-tile-content class="align-end">{{ address }}</v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>전화번호 :</v-list-tile-content>
        <v-list-tile-content class="align-end">{{ phone }}</v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>반려견 유무 :</v-list-tile-content>
        <v-list-tile-content class="align-end">{{ hasDogKr }}</v-list-tile-content>
      </v-list-tile>
      <v-list-tile>
        <v-list-tile-content>수정일자 :</v-list-tile-content>
        <v-list-tile-content class="align-end">{{ getDateAndTime(editedDate) }}</v-list-tile-content>
      </v-list-tile>
    </v-list>
  </div>
</template>

<script>
import { eventBus } from "../main"
import { dateFormat } from "../mixins/dateFormat"

export default {
  data () {
    return {
      editedDate : null
    }
  },
  props: {
    name: {
      type: String,
      required: true
    },
    address: {
      type: String,
      required: true
    },
    phone: {
      type: String,
      required: true
    },
    hasDog: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    hasDogKr() {
      return this.hasDog ? "있음" : "없음";
    }
  },
  methods: {
    switchName() {
      // this.nameOfChild = "컴퓨터"  // 부모컨포넌트에 의해 자식이 변경될수 있기 때문에 이 방식은 피해야한다.
    },
    // getDateAndTime(date) {
    //   if (date !== null) {
    //     let hour = date.getHours();
    //     let minutes = date.getMinutes();
    //     let fullDate = `${date.getFullYear()}/${date.getMonth() +
    //       1}/${date.getDate()}`;

    //     return `${fullDate} ${hour}:${minutes}`;
    //   } else {
    //     return;
    //   }
    // }
  },
  created() {
    eventBus.$on('userWasEdited', (date) => {
      this.editedDate = date
    })
  },
  mixins: [dateFormat]
};
</script>
