export const dateFormat = {
  data() {
    return {
      mixinData: "믹스인에서 선언된 데이터"
    }
  },
  methods: {
    getDateAndTime(date) {
      if (date !== null) {
        let hour = date.getHours();
        let minutes = date.getMinutes();
        let fullDate = `${date.getFullYear()}/${date.getMonth() +
          1}/${date.getDate()}`;

        return `${fullDate} ${hour}:${minutes}`;
      } else {
        return;
      }
    }
  }
}