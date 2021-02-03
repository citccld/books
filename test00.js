let origianData = {
  'OWS_FI': {
    'sum': 100,
    'return_list': [
      { 'service_name': 'GDE_ADC', 'cal_or_not': 'Y', 'group_package_size': 201 },
      { 'service_name': 'GDE_FS', 'cal_or_not': 'Y', 'group_package_size': 20 },
      { 'service_name': 'GDE_Manas', 'cal_or_not': 'Y', 'group_package_size': 30 },
      { 'service_name': 'GDE_Manas', 'cal_or_not': 'Y', 'group_package_size': 510 },
      { 'service_name': 'GDE_OS', 'cal_or_not': 'Y', 'group_package_size': 40 },
      { 'service_name': 'GDE_GKit', 'cal_or_not': 'Y', 'group_package_size': 45 },
    ]
  }
}

let selectMenu = 'OWS_FI_No_Manas'

if (selectMenu.indexOf('No_Manas') !== -1) {
  let selectName = selectMenu.split('_No_Manas')[0]
  // 把数组中的Manas中的cal_or_not值修改为N
  let arrList = origianData[selectName].return_list
  arrList.forEach((value, index, self) => {
    value.cal_or_not = value.service_name == 'GDE_Manas' ? 'N' : 'Y'
  })
  console.log(arrList)
}
