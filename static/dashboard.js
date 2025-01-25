async function fetchData() {
    try {
      const response = await fetch('/get_price_data'); // Fetch data from Flask API
      const data = await response.json();
  
      // Extract Yearly Prices (Bar Chart)
      const barChartLabels = data.yearly_prices.map(item => item.year);
      const barChartValues = data.yearly_prices.map(item => item.Modal_Price);
  
      // Extract Monthly Prices (Area Chart)
      const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
      const areaChartLabels = data.monthly_prices.map(item => monthNames[item.month]);
      const areaChartValues = data.monthly_prices.map(item => item.Modal_Price);
  
      // Bar Chart (Yearly Modal Price)
      const barChartOptions = {
        series: [{ data: barChartValues }],
        chart: {
            type: 'bar',
            height: 'auto', // Responsive height
            toolbar: { show: false }
          },
          plotOptions: { bar: { columnWidth: '50%' } },
        colors: ['#246dec', '#cc3c43', '#367952', '#f5b74f', '#4f35a1'],
       
        xaxis: { categories: barChartLabels, title: { text: 'Year' } },
        yaxis: { title: { text: 'Average Modal Price' } },
        responsive: [
            {
              breakpoint: 768,
              options: { chart: { height: 300 }, plotOptions: { bar: { columnWidth: '70%' } } }
            },
            {
              breakpoint: 576,
              options: { chart: { height: 250 }, plotOptions: { bar: { columnWidth: '80%' } } }
            }
          ]
      };
  
      const barChart = new ApexCharts(document.querySelector('#bar-chart'), barChartOptions);
      barChart.render();
  
      // Area Chart (Monthly Modal Price)
      const areaChartOptions = {
        series: [{ name: 'Modal Price', data: areaChartValues }],
        chart: {
            type: 'area',
            height: 'auto',
            toolbar: { show: false }
          },
        colors: ['#4f35a1'],
        stroke: { curve: 'smooth' },
        xaxis: { categories: areaChartLabels, title: { text: 'Month' } },
        yaxis: { title: { text: 'Average Modal Price' } },
        responsive: [
            { breakpoint: 768, options: { chart: { height: 300 } } },
            { breakpoint: 576, options: { chart: { height: 250 } } }
          ]
      };
      
  
      const areaChart = new ApexCharts(document.querySelector('#area-chart'), areaChartOptions);
      areaChart.render();
  
      const barChart2 = new ApexCharts(document.querySelector('#bar-chart2'), barChartOptions);
      barChart2.render();

    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }
  
  // Call fetchData when the page loads
  fetchData();
  