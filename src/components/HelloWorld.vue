<template>
  <div class="chart">
    <apexchart
      type="area"
      :options="chart.chartOptions"
      :series="chartSerie.series"
    ></apexchart>
    <div>
      <button @click="updateChart">Update!</button>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";
import { reactive } from 'vue';

export default {
  name: 'HelloWorld',
  components: {
    apexchart: VueApexCharts,
  },
  setup(){
    const chart = reactive({
      chartOptions: {
        chart: {
          width: '100%',
          id: "vuechart-example",
          type: 'area',
          stacked: false,
          zoom: {
            enabled: false
          },          
        },
        colors: ["#02182B"],
        dataLabels: {
          enabled: false
        },
        markers:{
          size: 0
        },
        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.45,
            opacityTo: 0.05,
            stops: [20, 100, 100, 100]            
          }
        },
        xaxis: {
          categories: [1578798000000,1581476400000,1583982000000,1586660400000,1589252400000,1591930800000,1594522800000,1597201200000],
          type: 'datetime',
          axisBorder: {
            show: false},
          axisTicks: {
            show: false},
          tooltip: {
              shared: true},
          legend: {
            position: 'top',
            horizontalAlign: 'right',
            offsetX: -10
          },        
        },
        yaxis: {
          labels: {
            formatter: function (value) {
              return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'BRL' }).format(value);
            },
          },
        },
      },
    });
    
    const chartSerie = reactive({
      series: [
        {
          name: "Bitcoin",
          data: [30, 40, 45, 50, 49, 60, 70, 99],
        }
      ],
    });

    async function updateChart() {
      let valores = await minhasbits();

      let bitcointValues = valores.map(function(valor) {return valor['closing']});
      let bitCoinDate = valores.map(function(valor) {return Date.parse(valor['date'])});

      const colors = ["#02182B"]; 

      chart.chartOptions = {
        colors: [colors[Math.floor(Math.random() * colors.length)]],
        xaxis:{
          categories : bitCoinDate
        }
      };
    
      chartSerie.series = [
        {
          data: bitcointValues,
        },
      ];
    }

    async function minhasbits(){
      let bitcoins = [];
      for (var i = 1; i <= 31; i++) {
            let a = await fetch(`https://www.mercadobitcoin.net/api/BTC/day-summary/2020/12/${i}`)
            .then(function(response) {
            return response.json();
            });
            bitcoins.push(a)
      }
      return bitcoins
    }

    return {updateChart, minhasbits, chart, chartSerie}
  }
}
</script>

<style lang="scss">

</style>
